ASSESSMENT = "ProgTest1"

# Directories
INPUT_DIRECTORY = f"./inputs/{ASSESSMENT}"
OUPTUT_DIRECTORY = "./outputs"
EPOST_DIRECTORY = "e_post"

# Some Course and Test Specific Information
COURSE = "EECS3342"
SEMESTER = "Fall 2025"
FEEDBACK_DIRECTORY = 3342
TOTAL_MARK = 100
CPS_WEIGHT = 15
DUE_DATE = "2025-10-01"
AVAILABLE_DATE = "2025-10-27"

# list of all 3 XLSX files to generate a combined ePost file. Else, declare a single xlsx file and a single a single relevant ePost file will be generated.
ALL_XLSX_FILE_MAP_PATHS_TO_SHEET_NAMES = {
    f"{INPUT_DIRECTORY}/EECS3342-F25-ProgTest1a-Grading-Sheet.xlsx": ["Proof Obligations", "Context C0A", "Machine HotelA"],
    f"{INPUT_DIRECTORY}/EECS3342-F25-ProgTest1b-Grading-Sheet.xlsx": ["Proof Obligations", "Context C0B", "Machine HotelB"],
}

EPOST_FILENAME_POSTFIX = "ePost"

# Additional params
NUM_OF_VERSIONS_OF_ASSESSMENT = 2