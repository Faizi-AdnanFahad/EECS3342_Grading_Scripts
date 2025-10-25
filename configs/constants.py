# define any new constants here or modify the constant values to match your system variables.

# Course Information
COURSE_NAME = "EECS 3342"
SEMESTER = "FALL"
YEAR_OF_TEACHING = "2025"
TEST_NAME = "Programming Test 1"
TEST_VERSION = "A"

# directories
GRADES_DIRECTORY = "ProgTest1"
INPUT_DIRECTORY = "./inputs"
OUTPUT_DIRECTORY = f"./outputs"

# xlsx file name
INDIVIDUAL_XLSX_FILE_PATH = f"{INPUT_DIRECTORY}/{GRADES_DIRECTORY}/EECS3342-F25-ProgTest1{TEST_VERSION.lower()}-Grading-Sheet.xlsx"  # Replace with your Excel file path that you want to check the assumptions on and generate `individual` feedback files for students
DETAILED_STUDENT_INFO_PATH = f"{INPUT_DIRECTORY}/EECS3342E"

# xlsx sheet names
MARKING_SCHEME_SHEET_NAME = f"Marking Scheme - ProgTest1{TEST_VERSION.lower()}"

SHEET_NAMES = {"Proof Obligations": 11, f"Context C0{TEST_VERSION}": 45, f"Machine Hotel{TEST_VERSION}": 44}

# other useful Constants
TA_COMMENT_HEADER_NAME = "TA Comment"

# Some Special Row and Column Numbers
GRADING_COMP_COLUMN = 0
INSTRUCTOR_COMMENT_COLUMN = 1
SPECIFIED_GRADE_COLUMN = 2

# total mark
TOTAL_MARKS = sum(SHEET_NAMES.values())
