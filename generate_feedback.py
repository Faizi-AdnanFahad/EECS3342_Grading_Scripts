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
    sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.PROOF_OBLIGATION_SHEET_NAME)
    print(helper.getEECSLogins(sheet))
    for login in helper.getEECSLogins(sheet):
        output_string += f"Student's EECS login: {login}\n"
        
        total_mark = 0
        output_string += f"Total marks received: {total_mark}\n"
        output_string += "Breakdown of Grading Results\n"
        
        output_string += "====================\n"
        proof_obligation_mark = 0
        output_string += f"Proof Obligations (subtotal: {proof_obligation_mark}/{constants.PROOF_OBLIGATION_TOTAL_MARK})\n"
        output_string += "====================\n"
        
        write_to_file(f"{constants.OUPTUT_DIRECTORY}/{login}.txt" , output_string)
        output_string = ""
