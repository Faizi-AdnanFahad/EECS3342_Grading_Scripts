import constants
import helper

# Specify the file path
file_path = f"{constants.OUPTUT_DIRECTORY}/test.txt"

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
        output_string += login +"\n";
    
    write_to_file(file_path, output_string)
