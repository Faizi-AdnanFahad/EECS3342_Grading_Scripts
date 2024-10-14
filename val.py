import openpyxl
import sys

XLSC_FILE_PATH = './input_files/EECS3342-F24-ProgTest1a-TA-Grading-Sheet.xlsx'  # Replace with your Excel file path
MARKING_SCHEME_NAME = 'Marking Scheme - ProgTest1a'
PROOF_OBLIGATION_SHEET_NAME = 'Proof Obligations'
CONTEXT_SHEET_NAME = 'Context C0A'
MACHINE_SHEET_NAME = 'Machine EnrollmentA'

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


if __name__ == "__main__":
        assumption1 = check_assumption1(MARKING_SCHEME_NAME)
        print(f"assumption 1: {assumption1}")
        print("==========================================================")
        assumption2 = check_assumption2(PROOF_OBLIGATION_SHEET_NAME, CONTEXT_SHEET_NAME, MACHINE_SHEET_NAME)
        print("assumption 2: ", assumption2)
        print("==========================================================")

