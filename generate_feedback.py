import configs.constants as constants
import helper

if __name__ == "__main__":
    # load sheet objects
    proof_obligation_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.PROOF_OBLIGATION_SHEET_NAME)
    context_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.CONTEXT_SHEET_NAME)
    machine_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.MACHINE_SHEET_NAME)
    
    # load grade data-structure for each sheet
    proof_obligation_data = helper.get_sheet_data(proof_obligation_sheet)
    context_data = helper.get_sheet_data(context_sheet)
    machine_data = helper.get_sheet_data(machine_sheet)
    
    grade_comp_to_specified_grades = helper.get_grading_component_mapping(constants.MARKING_SCHEME_SHEET_NAME)
    # print(grade_comp_to_specified_grades)    

    output_string = f"{constants.COURSE_NAME} {constants.SEMESTER} {constants.YEAR_OF_TEACHING} {constants.TEST_NAME} Grading Results\n"
    
    for student in proof_obligation_data:
        po_total_mark = helper.get_total_mark(student, proof_obligation_data)
        c_total_mark = helper.get_total_mark(student, context_data)
        m_total_mark = helper.get_total_mark(student, machine_data)
        
        output_string += f"Student's EECS login: {student}\n"
        
        output_string += f"Total marks received: {po_total_mark + c_total_mark + m_total_mark} (out of {constants.TOTAL_MARKS})\n"
        output_string += "Breakdown of Grading Results\n"
        
        output_string += "====================\n"
        output_string += f"Proof Obligations (subtotal: {po_total_mark}/{constants.SPECIFIED_PROOF_OBLIGATION_TOTAL_MARK})\n"
        output_string += "====================\n"
        for grade_comp, grade_comment_dict in proof_obligation_data[student].items():
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
        
        output_string += "====================\n"
        output_string += f"Context (subtotal: {c_total_mark}/{constants.SPECIFIED_CONTEXT_TOTAL_MARK})\n"
        output_string += "====================\n"
        for grade_comp, grade_comment_dict in context_data[student].items():
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

        output_string += "====================\n"
        output_string += f"Machine (subtotal: {m_total_mark}/{constants.SPECIFIED_MACHINE_TOTAL_MARK})\n"
        output_string += "====================\n"
        for grade_comp, grade_comment_dict in machine_data[student].items():
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
                        
        helper.write_to_file(f"{constants.OUPTUT_DIRECTORY}/{constants.GRADES_DIRECTORY}/{student}.txt" , output_string)
        output_string = ""
