# define any new constants here or modify the constant values to match your system variables.

# Course Information
COURSE_NAME = "EECS 3342"
SEMESTER = "FALL"
YEAR_OF_TEACHING = "2024"
TEST_NAME = "Programming Test 1"

# directories
INPUT_DIRECTORY = "./inputs"
OUPTUT_DIRECTORY = "./outputs"
GRADES_DIRECTORY = "grades"

# file names
INDIVIDUAL_XLSX_FILE_PATH = f"{INPUT_DIRECTORY}/EECS3342-F24-ProgTest1c-Grading-Sheet.xlsx"  # Replace with your Excel file path that you want to check the assumptions on and generate `individual` feedback files for students
DETAILED_STUDENT_INFO_PATH = f"{INPUT_DIRECTORY}/EECS3342E"

# sheet names
MARKING_SCHEME_SHEET_NAME = "Marking Scheme - ProgTest1c"
PROOF_OBLIGATION_SHEET_NAME = "Proof Obligations"
CONTEXT_SHEET_NAME = "Context C0C"
MACHINE_SHEET_NAME = "Machine EnrollmentC"

# list of all XLSX files to be marked
ALL_XLSX_FILE_MAP_PATHS_TO_SHEET_NAMES = {
    f"{INPUT_DIRECTORY}/EECS3342-F24-ProgTest1a-Grading-Sheet.xlsx": ["Proof Obligations", "Context C0A", "Machine EnrollmentA"],
    f"{INPUT_DIRECTORY}/EECS3342-F24-ProgTest1b-Grading-Sheet.xlsx": ["Proof Obligations", "Context C0B", "Machine EnrollmentB"],
}


# other useful Constants
TA_COMMENT_HEADER_NAME = "TA Comment"

# Some Special Row and Column Numbers
GRADING_COMP_COLUMN = 0
INSTRUCTOR_COMMENT_COLUMN = 1
SPECIFIED_GRADE_COLUMN = 2

# total marks
SPECIFIED_PROOF_OBLIGATION_TOTAL_MARK = 15
SPECIFIED_CONTEXT_TOTAL_MARK = 49
SPECIFIED_MACHINE_TOTAL_MARK = 36
TOTAL_MARKS = 100
