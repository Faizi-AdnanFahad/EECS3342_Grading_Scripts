# define any new constants here or modify the constant values to match your system variables.

# Course Information
COURSE_NAME = "EECS 3342"
SEMESTER = "FALL"
YEAR_OF_TEACHING = "2024"
TEST_NAME = "Programming Test 2"

# directories
GRADES_DIRECTORY = "ProgTest2"
INPUT_DIRECTORY = "./inputs"
OUTPUT_DIRECTORY = f"./outputs"

# xlsx file name
INDIVIDUAL_XLSX_FILE_PATH = f"{INPUT_DIRECTORY}/{GRADES_DIRECTORY}/EECS3342-F24-ProgTest2a-Grading-Sheet.xlsx"  # Replace with your Excel file path that you want to check the assumptions on and generate `individual` feedback files for students
DETAILED_STUDENT_INFO_PATH = f"{INPUT_DIRECTORY}/EECS3342E"

# xlsx sheet names
MARKING_SCHEME_SHEET_NAME = "Marking Scheme - ProgTest2a"

SHEET_NAMES = {"Proof Obligations": 30, "Context opA": 60, "Compilation-Errors": 10}

# other useful Constants
TA_COMMENT_HEADER_NAME = "TA Comment"

# Some Special Row and Column Numbers
GRADING_COMP_COLUMN = 0
INSTRUCTOR_COMMENT_COLUMN = 1
SPECIFIED_GRADE_COLUMN = 2

# total mark
TOTAL_MARKS = sum(SHEET_NAMES.values())
