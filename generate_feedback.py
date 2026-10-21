import configs.constants as constants
import Helpers.helper as helper
import validate

def generate_feedback():      
    # grade component -> specified grades by professor
    grade_comp_to_specified_grades = helper.get_grading_component_mapping(constants.MARKING_SCHEME_SHEET_NAME)

    # mapping of student eecs logins to their full name
    # {"studentid": {"first_name": firstname, "last_name": lastname}}
    id_to_full_name = helper.parse_student_file(constants.DETAILED_STUDENT_INFO_PATH)
    
    # get the version of the test the student took
    test_version = constants.INDIVIDUAL_XLSX_FILE_PATH.split("-")[2][-1] # get the last character of the assessment from xlsx file
    
    output_string = "" 
    # get a list of students from any sheets since student names are identical in all sheets as per `assumption2`
    students = helper.get_eecs_logins(helper.read_excel_file(constants.INDIVIDUAL_XLSX_FILE_PATH, "Proof Obligations"))
    
    # populate additional feedback information for each student 
    for student in students:
        output_string += f"{constants.COURSE_NAME} {constants.SEMESTER} {constants.YEAR_OF_TEACHING} {constants.TEST_NAME} Grading Results\n"
        output_string += f"Assessment Version: {test_version}\n"
        total_mark = helper.get_total_mark(student)
        
        full_name = id_to_full_name.get(student)
        if full_name is None:
            print(f"Warning: student '{student}' not found in {constants.DETAILED_STUDENT_INFO_PATH}; name will be blank.")
            first_name = ""
            last_name = ""
        else:
            first_name = full_name.get("first_name", "")
            last_name = full_name.get("last_name", "")
        
        output_string += f"Student's EECS login: {student}\n"
        output_string += f"Full Name: {last_name}, {first_name}\n"
        
        output_string += f"Total marks received: {total_mark} (out of {constants.TOTAL_MARKS})\n"
        output_string += "Breakdown of Grading Results\n"
        
        # populate detailed feedback for all sheets
        for sheet_name in constants.SHEET_NAMES.keys():
            curr_sheet_obj = helper.read_excel_file(constants.INDIVIDUAL_XLSX_FILE_PATH, sheet_name)
            # load grade data-structure for each sheet
            curr_sheet_data = helper.get_sheet_data(curr_sheet_obj)
            
            output_string += "====================\n"
            curr_sheet_total_mark = helper.get_total_mark_in_a_sheet(student, curr_sheet_data)
            output_string += f"{sheet_name} (subtotal: {curr_sheet_total_mark}/{constants.SHEET_NAMES.get(sheet_name)})\n"
            output_string += "====================\n"
            for grade_comp, grade_comment_dict in curr_sheet_data[student].items():
                given_grade = grade_comment_dict["given_grade"]
                ta_comment = grade_comment_dict["ta_comment"]
                specified_grade = grade_comp_to_specified_grades[grade_comp]["specified_grade"]
                instructor_comment = grade_comp_to_specified_grades[grade_comp]["instructor_comment"]
                
                output_string += f"{grade_comp}: {given_grade}/{specified_grade}\n"
                if ta_comment is not None:
                    output_string += f"TA Comment: {ta_comment}\n"
                if instructor_comment is not None:
                    output_string += f"Instructor' Comment: {instructor_comment}\n"
                output_string += "---\n"
                    
        helper.write_to_file(f"{constants.OUTPUT_DIRECTORY}/{constants.GRADES_DIRECTORY}/{student}.txt" , output_string)
        output_string = ""
        
if __name__ == "__main__":
    assumption1 = validate.check_assumption1(constants.MARKING_SCHEME_SHEET_NAME)
    assumption2 = validate.check_assumption2(constants.SHEET_NAMES)
    assumption3 = validate.check_assumption3(constants.MARKING_SCHEME_SHEET_NAME, constants.SHEET_NAMES)
    assumption4 = validate.check_assumption4(constants.MARKING_SCHEME_SHEET_NAME, constants.SHEET_NAMES)

    all_assumptions_satisifed = (
        assumption1 and assumption2 and assumption3 and assumption4
    )

    print("==========================================================")
    print(f"assumption 1: {assumption1}")
    print("==========================================================")
    print(f"assumption 2: {assumption2}")
    print("==========================================================")
    print(f"assumption 3: {assumption3}")
    print("==========================================================")
    print(f"assumption 4: {assumption4}")
    print("*****************************************************************")
    print(f"All Assumptions Passed? {all_assumptions_satisifed}")
    print("*****************************************************************")
    
    print("For detailed information about the assumptions, please look at the `assumptions.txt`")
    
    # generate feedback only if all assumptions are satisifed
    if all_assumptions_satisifed:
        generate_feedback()
    else:
        print("Feedbacks will not be generated! Please make sure that all assumptions are satisfied first")