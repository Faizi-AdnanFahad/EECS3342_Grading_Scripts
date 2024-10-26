import Helpers.helper as helper
import Helpers.epost_helper as epost_helper
import configs.constants
import configs.epost_config
import statistics

constants = configs.constants
epost_config = configs.epost_config


if __name__ == "__main__":
    output_string = f"+ {epost_config.COURSE} {epost_config.SEMESTER} {epost_config.ASSESSMENT}\n"
    output_string += f"+ To see feedback, run the command <b>feedback {epost_config.FEEDBACK_DIRECTORY}F {epost_config.ASSESSMENT}</b> on a remote labs terminal.\n"
    output_string += f"+ cutoff: A+={epost_config.TOTAL_MARK * 0.9}, A={epost_config.TOTAL_MARK * 0.8}, B+={epost_config.TOTAL_MARK * 0.75}, B={epost_config.TOTAL_MARK * 0.70}, C+={epost_config.TOTAL_MARK * 0.65}, C={epost_config.TOTAL_MARK * 0.6}, D+={epost_config.TOTAL_MARK * 0.55}, D={epost_config.TOTAL_MARK * 0.5}, E={epost_config.TOTAL_MARK * 0.45}, F={epost_config.TOTAL_MARK * 0}\n"
    
    # get student -> total grade mapping
    student_to_total_grade =  epost_helper.get_students_to_total_grade()
        
    # assuming the list of students are identical in all of the sheets
    students = list(student_to_total_grade.keys())
    
    output_string += f"+ count: {len(students)}:average: {statistics.mean(student_to_total_grade.values()):.1f},median: {statistics.median(student_to_total_grade.values())},min: {min(student_to_total_grade.values())},max:{max(student_to_total_grade.values())}\n"
    output_string += f"+ CPS weight={epost_config.CPS_WEIGHT:.1f}%: max={epost_config.TOTAL_MARK}: due={epost_config.DUE_DATE}: available={epost_config.AVAILABLE_DATE}\n"
    
    for student in students:
        output_string += f"{student} {student_to_total_grade.get(student):.2f}\n"
    
    e_post_filename = ""
    if len(epost_config.ALL_XLSX_FILE_MAP_PATHS_TO_SHEET_NAMES) == 1: # generate individual epost file
        xlsx_file_path = next(iter(epost_config.ALL_XLSX_FILE_MAP_PATHS_TO_SHEET_NAMES))
        
        # get the individual Assessment name from the xlsx file name - to be used as .epost filename
        e_post_filename_prefix = xlsx_file_path.split("-")[2]
        e_post_filename = f"{e_post_filename_prefix}.{epost_config.EPOST_FILENAME_POSTFIX}"
    elif len(epost_config.ALL_XLSX_FILE_MAP_PATHS_TO_SHEET_NAMES) == 3:
        e_post_filename = f"{epost_config.ASSESSMENT}.{epost_config.EPOST_FILENAME_POSTFIX}"
    else:
        print("Error: .ePost file can only be generated for either a single file or All 3 files")
        exit()
    
    helper.write_to_file(f"{epost_config.OUPTUT_DIRECTORY}/{epost_config.EPOST_DIRECTORY}/{e_post_filename}" , output_string)