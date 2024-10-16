import openpyxl
import constants

XLSC_FILE_PATH = constants.XLSC_FILE_PATH
MARKING_SCHEME_SHEET_NAME = constants.MARKING_SCHEME_SHEET_NAME
PROOF_OBLIGATION_SHEET_NAME = constants.PROOF_OBLIGATION_SHEET_NAME

# Given a file path and a sheet name, this function returns the sheet object.
def read_excel_file(file_path, sheet_name):
    try:
        # Load the workbook and select the specified sheet
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        return sheet;
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError:
        print(f"Error: The sheet '{sheet_name}' does not exist in the workbook.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# Helper Method
# Given a sheet name, this function iterates over each row in the first column of `sheet` 
# which is assumed to have the eecs logins and acummulate them to return a list of eecs logins
def get_eecs_logins(sheet):
    eecs_logins_from_PO = []
    for row in sheet.iter_rows(values_only=True):
        if any(value is not None for value in row):
            col1 = row[0]
            if col1 != "EECS Login": #if actual logins, add it to the list obtained from the first cheetsheet
                eecs_logins_from_PO.append(col1)
    return eecs_logins_from_PO

# helper
# mapping of grading component -> Max numerical mark
def get_grading_component_mapping(m_scheme_sheet_name):
    grade_component_dict = {}
    marking_scheme_sheet = read_excel_file(XLSC_FILE_PATH, m_scheme_sheet_name)
    for row in marking_scheme_sheet.iter_rows(values_only=True):
        if is_a_grading_component(row):
            grade_component_name = row[constants.GRADING_COMP_COLUMN]
            assigned_mark = row[constants.SPECIFIED_GRADE_COLUMN]
            # If the key already exists in the dictionary, append the item to the list
            if grade_component_name in grade_component_dict:
                grade_component_dict[grade_component_name].append(assigned_mark)
            # If the key does not exist, create a new list with the item
            else:
                grade_component_dict[grade_component_name] = [assigned_mark]
    
    return grade_component_dict

# Given a row, return true if its a grading component.
# a row is a grading component if its first col's value is a string and it's second col's value is an float.
def is_a_grading_component(row):
    grading_component = row[constants.GRADING_COMP_COLUMN]
    specified_grade = row[constants.SPECIFIED_GRADE_COLUMN]
    
    if isinstance(specified_grade, int):
        specified_grade = float(specified_grade)
        
    if isinstance(grading_component, str) and isinstance(specified_grade, float):
         return True
    else:
         return False
    
# Given a sheet object, this function returns a datastructure that will include the list of all eecs_logins for students
# alongside a mapping of the grading components and the given mark to them in the following format.
# grades = {"studentlogin1": {"thm1/THM": 1, "thm2/THM": 2, ...}, "studentlogin2": {"thm1/THM": 1, "thm2/THM": 2, ...}...}
def get_sheet_data(sheet):
    grades = {}
    
    header_row = next(sheet.iter_rows(min_row=1, max_row=1, min_col=1, values_only=True))
    
    # skip the header row'    
    for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
        if any(value is not None for value in row): # if all value of the row is not NONE
            for i in range(1, len(row), 2):
                student_login = row[0] # student login assumed to be in column 1 as per assumption1
                grading_comp = header_row[i]
                given_grade = row[i]
                ta_comment = row[i + 1]            

                if student_login not in grades:
                    initial_grade = {}
                    initial_grade[grading_comp] = {"given_grade": given_grade, "ta_comment": ta_comment}
                    grades[student_login] = initial_grade
                else:
                    existing_grades = grades[student_login]
                    if grading_comp not in existing_grades:
                        existing_grades[grading_comp] = {"given_grade": given_grade, "ta_comment": ta_comment}
                
    return grades

# Given a sheet object and mapping of grading component to specified grades, the function checkes
# if the given grades are within the constrains of the specified grades
def is_constrained(sheet, grade_comp_to_grade):
    grades = get_sheet_data(sheet)
    for student_login in grades:
        grade_comp_to_given_grade_mappings = grades[student_login]
        for grading_comp, given_grade in grade_comp_to_given_grade_mappings.items():
            specified_grade = grade_comp_to_grade.get(grading_comp)[0] # the returned will always be a list of
            if 0 <= given_grade and given_grade <= specified_grade:
                continue
            else:
                print(f"Error: Grade given for studnet `{student_login}` is outside the allowable grade for ({grading_comp} -> {given_grade})")
                return False
    return True

def get_total_mark(student_login, grades):
    total = 0
    student_marks = grades[student_login]
    for given_grade in student_marks.values():
        total += given_grade["given_grade"]
    return total