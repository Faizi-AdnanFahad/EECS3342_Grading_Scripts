import constants

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
    
    
    write_to_file(file_path, output_string)
