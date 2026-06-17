from services import faults_service

def run_cli():

    while True:
        print("\n1. Показать ошибки")
        print("2. Найти ошибку")
        print("3. Выход\n")

        choice = input("Выберите действие: ")

        if choice == "1":
            all_faults = faults_service.get_all_faults()
            faults_service.print_all_faults(all_faults)

        elif choice == "2":
            fault_code = input("Введите код ошибки: ")
            fault_data = faults_service.find_fault(faults_service.faults,fault_code)
            faults_service.print_fault(fault_code, fault_data)

        elif choice == "3":
            break

        else:
            print("Неизвестная команда") 