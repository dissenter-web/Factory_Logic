from app.services.faults_service import get_all_faults, find_fault
from app.services.spare_parts_service import find_spare_part
from app.formatters.spare_parts_formatter import format_spare_part
from app.formatters.fault_formatter import format_fault, format_all_faults

def find_fault_action(list_faults,fault_code):
    fault_data = find_fault(list_faults, fault_code)
    print(format_fault(fault_code, fault_data))

def get_all_faults_action(list_faults):
    all_faults = get_all_faults(list_faults)
    print(format_all_faults(all_faults))

def find_spare_part_action(spare_part, list_spare_parts):
    spare_part_data = find_spare_part(list_spare_parts, spare_part)
    print(*format_spare_part(spare_part, spare_part_data))