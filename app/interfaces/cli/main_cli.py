from services import faults_service
from formatters.fault_formatter import format_fault, format_all_faults

def run_cli():

    while True:
        print("\n1. Показать ошибки")
        print("2. Найти ошибку")
        print("3. Выход\n")

        choice = input("Выберите действие: ")

        if choice == "1":
            all_faults = faults_service.get_all_faults()
            print(format_all_faults(all_faults))

        elif choice == "2":
            fault_code = input("Введите код ошибки: ")
            fault_data = faults_service.find_fault(fault_code)
            print(format_fault(fault_code.upper(), fault_data))

        elif choice == "3":
            break

        else:
            print("Неизвестная команда") 