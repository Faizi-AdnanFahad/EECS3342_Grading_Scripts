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
def getEECSLogins(sheet):
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