import constants
import helper

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:  # Open the file in write mode
            file.write(content)  # Write the content to the file
        print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    output_string = "EECS3342 Fall 2024 ProgTest1 Grading Results\n"
    po_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.PROOF_OBLIGATION_SHEET_NAME)
    context_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.CONTEXT_SHEET_NAME)
    machine_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.MACHINE_SHEET_NAME)
    
    for login in helper.getEECSLogins(po_sheet):
        po_total_mark = helper.get_total_mark(login, po_sheet)
        c_total_mark = helper.get_total_mark(login, context_sheet)
        m_total_mark = helper.get_total_mark(login, machine_sheet)
        
        output_string += f"Student's EECS login: {login}\n"
        
        output_string += f"Total marks received: {po_total_mark + c_total_mark + m_total_mark}\n"
        output_string += "Breakdown of Grading Results\n"
        
        output_string += "====================\n"
        output_string += f"Proof Obligations (subtotal: {po_total_mark}/{constants.SPECIFIED_PROOF_OBLIGATION_TOTAL_MARK})\n"
        output_string += "====================\n"
        
        write_to_file(f"{constants.OUPTUT_DIRECTORY}/{login}.txt" , output_string)
        output_string = ""
