import openpyxl
import sys

# Function to read an Excel file and iterate over its rows
def read_excel_file(file_path, sheet_name):
    try:
        # Load the workbook and select the specified sheet
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        
        # Iterate over the rows in the sheet (excluding the header row if necessary)
        return sheet;

                
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError:
        print(f"Error: The sheet '{sheet_name}' does not exist in the workbook.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

def check_assumption1():
    sheet = read_excel_file(file_path, sheet_name)
     
    subtotal = 0
    for row in sheet.iter_rows(values_only=True):
        if is_a_grading_component(row):    
            specifiedGrade = row[1]
            subtotal += specifiedGrade
            
    if subtotal != 100:
        return False
    else:
        return True

def is_a_grading_component(row):
    col1 = row[0]
    col2 = row[1]
    if isinstance(col1, str) and isinstance(col2, int):
         return True
    else:
         return False
         


if __name__ == "__main__":
        # Example usage:
        file_path = './input_files/EECS3342-F24-ProgTest1a-TA-Grading-Sheet.xlsx'  # Replace with your Excel file path
        sheet_name = 'Marking Scheme - ProgTest1a'       # Replace with your desired sheet name
        # Call the function to read the Excel file
        
        assumption1 = check_assumption1()
        print("assumption 1: ", assumption1)
