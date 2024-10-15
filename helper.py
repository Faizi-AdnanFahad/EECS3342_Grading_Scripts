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