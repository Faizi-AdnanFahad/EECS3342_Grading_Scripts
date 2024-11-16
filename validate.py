import openpyxl
import configs.constants as constants
import Helpers.helper as helper

XLSC_FILE_PATH = constants.INDIVIDUAL_XLSX_FILE_PATH

# assumption 1:
# Checks the assumption that the assigned marks for all grading components add up to TOTAL_MARK=100
def check_assumption1(sheet_name):
    marking_scheme_sheet = helper.read_excel_file(XLSC_FILE_PATH, sheet_name)
    subtotal = 0
    for row in marking_scheme_sheet.iter_rows(values_only=True):
        if helper.is_a_grading_component(row):
            specifiedGrade = row[constants.SPECIFIED_GRADE_COLUMN]
            subtotal += specifiedGrade

    if subtotal != constants.TOTAL_MARKS:
        print(f"Error: specified grade total is not equal to {constants.TOTAL_MARKS}")
        return False
    else:
        return True


# assumption 2:
# Assuming that the 1st column of sheets always contains the EECS logins of all students taking that version of test.
# This function returns true if the 1st columns of all sheets are identical, false otherwise.
def check_assumption2(sheets):
    eecs_logins = []
    for sheet_names in sheets.keys():
        current_sheet_obj = helper.read_excel_file(XLSC_FILE_PATH, sheet_names)
        current_eecs_logins = helper.get_eecs_logins(current_sheet_obj)
        eecs_logins.append(current_eecs_logins)
    
    identical = all(sublist == eecs_logins[0] for sublist in eecs_logins) 
    
    if identical:
        return True
    else:
        print(f"Error: Student logins aren't identical in all sheets.")
        return False
    return 


# Assumption 3
# Except the first column, Headers of subsequent columns come in pairs in sheets: grading components and "TA Comment".
# Grading component names should match ones specified in assumption_1.
def check_assumption3(m_scheme_sheet_name, sheets):
    grade_component_list = list(
        helper.get_grading_component_mapping(m_scheme_sheet_name).keys()
    )

    for sheet_name in sheets.keys():
        current_sheet_obj = helper.read_excel_file(XLSC_FILE_PATH, sheet_name)
        first_row_p_sheet =  current_sheet_obj[1]
        first_row_values = tuple([cell.value for cell in first_row_p_sheet if cell.value is not None])
        
        # does sheet have valid header names
        has_valid_headers = is_valid_header(
            first_row_values, grade_component_list
        )
        
        # does grading com
        comes_in_pair = headers_come_in_pair(first_row_values)
        if not has_valid_headers or not comes_in_pair:
            if not has_valid_headers:
                print(f"Error: `{sheet_name}` sheet does not have valid headers.")

            if not comes_in_pair:
                print(f"Error: `{sheet_name}` sheet does not come in pairs.")
            return False
    
    return True

# assumption 4
# For each row, corresponding to marks that student receives, the numerical value should be constrained by the assigned marks for that grading component.
def check_assumption4(m_scheme_sheet_name, sheets):
    grade_comp_to_grade = helper.get_grading_component_mapping(m_scheme_sheet_name)
    for sheet_name in sheets.keys():
        current_sheet_obj = helper.read_excel_file(XLSC_FILE_PATH, sheet_name)
        is_sheet_constrained = helper.is_constrained(current_sheet_obj, grade_comp_to_grade)
        if not is_sheet_constrained:
            print(
                f"Error: Given mark in `{sheet_name}` sheet, is outside of the specified mark in `{m_scheme_sheet_name}` sheet."
            )
            return False
    
    return True

# Helper method that checks to see if header is a valid header.
# Valid headers are the ones specified in the marking scheme sheet
def is_valid_header(headers_tuple, grading_component_list):
    for i in range(1, len(headers_tuple) - 1, 2):
        current_grading_component = headers_tuple[i]
        if current_grading_component == "None" or current_grading_component not in grading_component_list:
            print(
                f"Error: '{current_grading_component}' is not a valid grading component."
            )
            return False
    return True


# helper method that checks if the headers come in pairs such that each grading component is followed by a TA Comment
def headers_come_in_pair(headers_tuple):
    # Skip the first column and check the rest in pairs
    for i in range(1, len(headers_tuple) - 1, 2):
        grading_component = headers_tuple[i]
        ta_comment = headers_tuple[i + 1]

        # Check if the second element of the pair is "TA Comment"
        if ta_comment != constants.TA_COMMENT_HEADER_NAME:
            print(
                f"Error: '{grading_component}' is not followed by `{constants.TA_COMMENT_HEADER_NAME}` column."
            )
            return False

    # print(f"All grading components are correctly followed by {constants.TA_COMMENT_HEADER_NAME}.")
    return True
