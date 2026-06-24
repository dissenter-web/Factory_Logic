def normalize_fault_code(fault_code):
    return fault_code.strip().upper()

def find_fault(faults, fault_code):
    fault_code = normalize_fault_code(fault_code)
    return faults.get(fault_code)

def get_all_faults(faults):
    return faults