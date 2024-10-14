import openpyxl
import constants

XLSC_FILE_PATH = constants.XLSC_FILE_PATH
MARKING_SCHEME_SHEET_NAME = constants.MARKING_SCHEME_SHEET_NAME
PROOF_OBLIGATION_SHEET_NAME = constants.PROOF_OBLIGATION_SHEET_NAME
CONTEXT_SHEET_NAME = constants.CONTEXT_SHEET_NAME
MACHINE_SHEET_NAME = constants.MACHINE_SHEET_NAME

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
        

# assumption 1: 
# Checks the assumption that the assigned marks for all grading components add up to TOTAL_MARK=100
def check_assumption1(sheet_name):
    TOTAL_MARK = 100
    marking_scheme_sheet = read_excel_file(XLSC_FILE_PATH, sheet_name)
     
    subtotal = 0
    for row in marking_scheme_sheet.iter_rows(values_only=True):
        if is_a_grading_component(row):    
            specifiedGrade = row[1]
            subtotal += specifiedGrade 
            
    if subtotal != TOTAL_MARK:
        return False
    else:
        return True

# assumption 2: 
# Assuming that the 1st column contains the EECS logins of all students taking that version of test.
# This function returns true if the 1st columns of all three sheets is identical, false otherwise.
def check_assumption2(po_sheet_name, c_sheet_name, m_sheet_name):
    proof_obligation_sheet = read_excel_file(XLSC_FILE_PATH, po_sheet_name)
    context_sheet = read_excel_file(XLSC_FILE_PATH, c_sheet_name)
    machine_sheet = read_excel_file(XLSC_FILE_PATH, m_sheet_name)
    
    # get the list of eecs logins in each sheet
    eecs_logins_from_PO = getEECSLogins(proof_obligation_sheet)
    eecs_logins_from_context = getEECSLogins(context_sheet)
    eecs_logins_from_machine = getEECSLogins(machine_sheet)
    
    return eecs_logins_from_PO == eecs_logins_from_context == eecs_logins_from_machine


def check_assumption3(m_scheme_sheet_name, po_sheet_name, c_sheet_name, m_sheet_name):
    grade_component_list = list(get_grading_component_mapping(m_scheme_sheet_name).keys())

    # proof obligation
    proof_obligation_sheet = read_excel_file(XLSC_FILE_PATH, po_sheet_name)
    first_row_po_sheet = next(proof_obligation_sheet.iter_rows(values_only=True, max_row=1)) # headers ROW for PO Sheet
    valid_header_PO = is_valid_header(first_row_po_sheet, grade_component_list) # valid headers for Proof obligation
    pairs_PO = headers_come_in_pair(first_row_po_sheet)
    
    if not valid_header_PO or not pairs_PO:
        if not valid_header_PO:
            print(f"Error: `{po_sheet_name}` sheet does not have valid headers.")
        
        if not pairs_PO:
            print(f"Error: `{po_sheet_name}` sheet does not come in pairs.")
        return False

    # context
    contxt_sheet = read_excel_file(XLSC_FILE_PATH, c_sheet_name)
    first_row_c_sheet = next(contxt_sheet.iter_rows(values_only=True, max_row=1)) # headers ROW for context Sheet
    valid_header_c = is_valid_header(first_row_c_sheet, grade_component_list) # valid headers for context
    pairs_c = headers_come_in_pair(first_row_c_sheet)
    if not valid_header_c or not pairs_c:
        if not valid_header_c:
            print(f"Error: `{c_sheet_name}` sheet does not have valid headers.")
        
        if not pairs_c:
            print(f"Error: `{c_sheet_name}` sheet does not come in pairs.")
        return False
    
    # machine
    machine_sheet = read_excel_file(XLSC_FILE_PATH, m_sheet_name)
    first_row_m_sheet = next(machine_sheet.iter_rows(values_only=True, max_row=1)) # headers ROW for context Sheet
    valid_header_m = is_valid_header(first_row_m_sheet, grade_component_list) # valid headers for context
    pairs_m = headers_come_in_pair(first_row_m_sheet)
    
    if not valid_header_m or not pairs_m:
        if not valid_header_m:
            print(f"Error: `{m_sheet_name}` sheet does not have valid headers.")
        
        if not pairs_m:
            print(f"Error: `{m_sheet_name}` sheet does not come in pairs.")
        return False
    
    return True

# Given a row, return true if its a grading component.
# a row is a grading component if its first col's value is a string and it's second col's value is an integer.
def is_a_grading_component(row):
    col1 = row[0]
    col2 = row[1]
    if isinstance(col1, str) and isinstance(col2, int):
         return True
    else:
         return False

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

def is_valid_header(headers_tuple, grading_component_list):
    for i in range(1, len(headers_tuple) - 1, 2):
        current_grading_component = headers_tuple[i]
        if current_grading_component not in grading_component_list:
            print(f"Error: '{current_grading_component}' is not a valid grading component.")
            return False
    return True

def headers_come_in_pair(headers_tuple):
    # Skip the first column and check the rest in pairs
    for i in range(1, len(headers_tuple) - 1, 2):
        grading_component = headers_tuple[i]
        ta_comment = headers_tuple[i + 1]

        # Check if the second element of the pair is "TA Comment"
        if ta_comment != constants.TA_COMMENT_HEADER_NAME:
            print(f"Error: '{grading_component}' is not followed by `{constants.TA_COMMENT_HEADER_NAME}` column.")
            return False

    # print(f"All grading components are correctly followed by {constants.TA_COMMENT_HEADER_NAME}.")
    return True


# helper
# mapping of grading component -> Max numerical mark
def get_grading_component_mapping(m_scheme_sheet_name):
    grade_component_dict = {}
    marking_scheme_sheet = read_excel_file(XLSC_FILE_PATH, m_scheme_sheet_name)
    for row in marking_scheme_sheet.iter_rows(values_only=True):
        if is_a_grading_component(row):
            grade_component_name = row[0]
            assigned_mark = row[1]
            # If the key already exists in the dictionary, append the item to the list
            if grade_component_name in grade_component_dict:
                grade_component_dict[grade_component_name].append(assigned_mark)
            # If the key does not exist, create a new list with the item
            else:
                grade_component_dict[grade_component_name] = [assigned_mark]
    
    return grade_component_dict

if __name__ == "__main__":
        assumption1 = check_assumption1(MARKING_SCHEME_SHEET_NAME)
        print(f"assumption 1: {assumption1}")
        print("==========================================================")
        assumption2 = check_assumption2(PROOF_OBLIGATION_SHEET_NAME, CONTEXT_SHEET_NAME, MACHINE_SHEET_NAME)
        print("assumption 2: ", assumption2)
        print("==========================================================")
        assumption3 = check_assumption3(MARKING_SCHEME_SHEET_NAME, PROOF_OBLIGATION_SHEET_NAME, CONTEXT_SHEET_NAME, MACHINE_SHEET_NAME)
        print("assumption 3: ", assumption3)
        print("==========================================================")
        
        # print(get_grading_component_mapping(MARKING_SCHEME_SHEET_NAME))
