import constants
import helper

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:  # Open the file in write mode
            file.write(content)  # Write the content to the file
        print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # load sheet objects
    proof_obligation_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.PROOF_OBLIGATION_SHEET_NAME)
    context_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.CONTEXT_SHEET_NAME)
    machine_sheet = helper.read_excel_file(constants.XLSC_FILE_PATH, constants.MACHINE_SHEET_NAME)
    
    # load grade data-structure for each sheet
    proof_obligation_grade = helper.get_grade_for_students(proof_obligation_sheet)
    context_grade = helper.get_grade_for_students(context_sheet)
    machine_grade = helper.get_grade_for_students(machine_sheet)
    
    grade_comp_to_specified_grades = helper.get_grading_component_mapping(constants.MARKING_SCHEME_SHEET_NAME)
    # print(grade_comp_to_specified_grades)    

    output_string = "EECS3342 Fall 2024 ProgTest1 Grading Results\n"
    
    for student in proof_obligation_grade:
        po_total_mark = helper.get_total_mark(student, proof_obligation_sheet, proof_obligation_grade)
        c_total_mark = helper.get_total_mark(student, context_sheet, context_grade)
        m_total_mark = helper.get_total_mark(student, machine_sheet, machine_grade)
        
        output_string += f"Student's EECS login: {student}\n"
        
        output_string += f"Total marks received: {po_total_mark + c_total_mark + m_total_mark}\n"
        output_string += "Breakdown of Grading Results\n"
        
        output_string += "====================\n"
        output_string += f"Proof Obligations (subtotal: {po_total_mark}/{constants.SPECIFIED_PROOF_OBLIGATION_TOTAL_MARK})\n"
        output_string += "====================\n"
        for grade_comp, given_grade in proof_obligation_grade[student].items():
            specified_grade = grade_comp_to_specified_grades[grade_comp][0]
            output_string += f"{grade_comp}: {given_grade}/{specified_grade}\n"
        
        output_string += "====================\n"
        output_string += f"Context (subtotal: {c_total_mark}/{constants.SPECIFIED_CONTEXT_TOTAL_MARK})\n"
        output_string += "====================\n"
        for grade_comp, given_grade in proof_obligation_grade[student].items():
            specified_grade = grade_comp_to_specified_grades[grade_comp][0]
            output_string += f"{grade_comp}: {given_grade}/{specified_grade}\n"
        
        output_string += "====================\n"
        output_string += f"Machine (subtotal: {m_total_mark}/{constants.SPECIFIED_MACHINE_TOTAL_MARK})\n"
        output_string += "====================\n"
        
        write_to_file(f"{constants.OUPTUT_DIRECTORY}/{student}.txt" , output_string)
        output_string = ""
