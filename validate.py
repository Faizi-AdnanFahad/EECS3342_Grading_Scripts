import openpyxl
import constants
import helper

XLSC_FILE_PATH = constants.XLSC_FILE_PATH
MARKING_SCHEME_SHEET_NAME = constants.MARKING_SCHEME_SHEET_NAME
PROOF_OBLIGATION_SHEET_NAME = constants.PROOF_OBLIGATION_SHEET_NAME
CONTEXT_SHEET_NAME = constants.CONTEXT_SHEET_NAME
MACHINE_SHEET_NAME = constants.MACHINE_SHEET_NAME

# assumption 1: 
# Checks the assumption that the assigned marks for all grading components add up to TOTAL_MARK=100
def check_assumption1(sheet_name):
    TOTAL_MARK = 100
    marking_scheme_sheet = helper.read_excel_file(XLSC_FILE_PATH, sheet_name)
     
    subtotal = 0
    for row in marking_scheme_sheet.iter_rows(values_only=True):
        if helper.is_a_grading_component(row):    
            specifiedGrade = row[constants.SPECIFIED_GRADE_COLUMN]
            subtotal += specifiedGrade 
    
    if subtotal != TOTAL_MARK:
        return False
    else:
        return True

# assumption 2: 
# Assuming that the 1st column contains the EECS logins of all students taking that version of test.
# This function returns true if the 1st columns of all three sheets is identical, false otherwise.
def check_assumption2(po_sheet_name, c_sheet_name, m_sheet_name):
    proof_obligation_sheet = helper.read_excel_file(XLSC_FILE_PATH, po_sheet_name)
    context_sheet = helper.read_excel_file(XLSC_FILE_PATH, c_sheet_name)
    machine_sheet = helper.read_excel_file(XLSC_FILE_PATH, m_sheet_name)
    
    # get the list of eecs logins in each sheet
    eecs_logins_from_PO = helper.getEECSLogins(proof_obligation_sheet)
    eecs_logins_from_context = helper.getEECSLogins(context_sheet)
    eecs_logins_from_machine = helper.getEECSLogins(machine_sheet)
    
    return eecs_logins_from_PO == eecs_logins_from_context == eecs_logins_from_machine


def check_assumption3(m_scheme_sheet_name, po_sheet_name, c_sheet_name, m_sheet_name):
    grade_component_list = list(helper.get_grading_component_mapping(m_scheme_sheet_name).keys())

    # proof obligation
    proof_obligation_sheet = helper.read_excel_file(XLSC_FILE_PATH, po_sheet_name)
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
    contxt_sheet = helper.read_excel_file(XLSC_FILE_PATH, c_sheet_name)
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
    machine_sheet = helper.read_excel_file(XLSC_FILE_PATH, m_sheet_name)
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

def check_assumption4(m_scheme_sheet_name, po_sheet_name, c_sheet_name, m_sheet_name):
    # get all of the xlsx sheets
    grade_comp_to_grade = helper.get_grading_component_mapping(m_scheme_sheet_name)    

    proof_obligation_sheet = helper.read_excel_file(XLSC_FILE_PATH, po_sheet_name)
    context_sheet = helper.read_excel_file(XLSC_FILE_PATH, c_sheet_name)
    machine_sheet = helper.read_excel_file(XLSC_FILE_PATH, m_sheet_name)
    
    po_sheet_constrained = helper.is_constrained(proof_obligation_sheet, grade_comp_to_grade)
    c_sheet_constrained = helper.is_constrained(context_sheet, grade_comp_to_grade)
    m_sheet_constrained = helper.is_constrained(machine_sheet, grade_comp_to_grade)

    if not po_sheet_constrained or not c_sheet_constrained or not m_sheet_constrained:
        if not po_sheet_constrained:
            print(f"Error: Given mark in `{po_sheet_name}` sheet, is outside of the specified mark in `{m_scheme_sheet_name}` sheet.")
        if not c_sheet_constrained:
            print(f"Error: Given mark in `{c_sheet_name}` sheet, is outside of the specified mark in `{m_scheme_sheet_name}` sheet.")
        if not m_sheet_constrained:
            print(f"Error: Given mark in `{m_sheet_name}` sheet, is outside of the specified mark in `{m_scheme_sheet_name}` sheet.")
        return False
    return True


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


if __name__ == "__main__":
        # assumption1 = check_assumption1(MARKING_SCHEME_SHEET_NAME)
        # print(f"assumption 1: {assumption1}")
        # print("==========================================================")
        # assumption2 = check_assumption2(PROOF_OBLIGATION_SHEET_NAME, CONTEXT_SHEET_NAME, MACHINE_SHEET_NAME)
        # print("assumption 2: ", assumption2)
        # print("==========================================================")
        # assumption3 = check_assumption3(MARKING_SCHEME_SHEET_NAME, PROOF_OBLIGATION_SHEET_NAME, CONTEXT_SHEET_NAME, MACHINE_SHEET_NAME)
        # print("assumption 3: ", assumption3)
        # print("==========================================================")
        assumption4 = check_assumption4(MARKING_SCHEME_SHEET_NAME, PROOF_OBLIGATION_SHEET_NAME, CONTEXT_SHEET_NAME, MACHINE_SHEET_NAME)
        print("assumption 4: ", assumption4)
        # print("==========================================================")
        # print(helper.get_grading_component_mapping(MARKING_SCHEME_SHEET_NAME))]
        print("hi")
        # grades = get_grade_for_students(helper.read_excel_file(constants.XLSC_FILE_PATH, constants.PROOF_OBLIGATION_SHEET_NAME))
        # print(grades)
        # print(grades['aliverdi'])