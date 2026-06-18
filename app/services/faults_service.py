from repositories.json_repository import load_faults

def find_fault(fault_code):
    faults = load_faults()
    fault_code = fault_code.upper()
    return faults.get(fault_code)

def get_all_faults():
    return load_faults()