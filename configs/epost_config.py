# Directories
INPUT_DIRECTORY = "./inputs"
OUPTUT_DIRECTORY = "./outputs"
EPOST_DIRECTORY = "e_post"

# Some Course and Test Specific Information
COURSE = "EECS3342"
SEMESTER = "Fall 2024"
ASSESSMENT = "ProgTest1"
FEEDBACK_DIRECTORY = 3342
TOTAL_MARK = 30
CPS_WEIGHT = 5
DUE_DATE = "2022-10-04"
AVAILABLE_DATE = "2022-10-18"

# list of all 3 XLSX files to generate a combined ePost file. Else, declare a single xlsx file and a single a single relevant ePost file will be generated.
ALL_XLSX_FILE_MAP_PATHS_TO_SHEET_NAMES = {
    f"{INPUT_DIRECTORY}/EECS3342-F24-ProgTest1b-Grading-Sheet.xlsx": ["Proof Obligations", "Context C0B", "Machine EnrollmentB"]
}

EPOST_FILENAME_POSTFIX = "ePost"