import configs.epost_config as epost_configs
import Helpers.helper as helper

def get_students_to_total_grade():
    result = {}
    for XLSX_FILE_PATH, SHEET_NAMES in epost_configs.ALL_XLSX_FILE_MAP_PATHS_TO_SHEET_NAMES.items():
        # load sheet objects
        proof_obligation_sheet = helper.read_excel_file(XLSX_FILE_PATH, SHEET_NAMES[0])
        context_sheet = helper.read_excel_file(XLSX_FILE_PATH, SHEET_NAMES[1])
        machine_sheet = helper.read_excel_file(XLSX_FILE_PATH, SHEET_NAMES[2])
    
        # load grade data-structure for each sheet
        proof_obligation_data = helper.get_sheet_data(proof_obligation_sheet)
        context_data = helper.get_sheet_data(context_sheet)
        machine_data = helper.get_sheet_data(machine_sheet)
    
        students = list(proof_obligation_data.keys())
    
        for student in students:
            po_total_mark = helper.get_total_mark_in_a_sheet(student, proof_obligation_data)
            c_total_mark = helper.get_total_mark_in_a_sheet(student, context_data)
            m_total_mark = helper.get_total_mark_in_a_sheet(student, machine_data)
        
            result[student] = po_total_mark + c_total_mark + m_total_mark
        
    return result