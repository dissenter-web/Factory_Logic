from app.services import faults_service, spare_parts_service
from app.formatters.fault_formatter import format_fault, format_all_faults
from app.repositories import json_repository

def run_cli():

    while True:
        print("\n1. VFD")
        print("2. Запасные части")
        print("3. Выход\n")

        choice = input("Выберите действие: ")

        if choice == "1":
            print("\n1. Allen_Bradley")
            print("2. ABB")
            print("3. SEW_Eurodrive")
            print("4. Выход\n")

            choice = input("Выберите производителя VFD: ")

            if choice == "1":
                manufacturer = "allen_bradley"
                print("\n1. PF525")
                print("2. PF40")
                print("3. PF753")
                print("3. PF160")
                print("4. Выход\n")

                choice = input("Выберите модель VFD: ")

                if choice == "1":
                    model = "pf525"
                    data_type = "faults"
                    faults = json_repository.load_vfd_data(manufacturer, model, data_type)
                    print("\n1. Показать все ошибки")
                    print("2. Найти ошибку по коду")
                    print("3. Выход\n")

                    choice = input("Выберите действие: ")

                    if choice == "1":
                        all_faults = faults_service.get_all_faults(faults)
                        print(format_all_faults(all_faults))

                    elif choice == "2":
                        fault_code = faults_service.normalize_fault_code(input("Введите код ошибки: "))
                        fault_data = faults_service.find_fault(faults, fault_code)
                        print(format_fault(fault_code.upper(), fault_data))

                    elif choice == "3":
                        break

            elif choice == "2":
                pass

            elif choice == "3":
                pass

            elif choice == "4":
                break

        elif choice == "2":
            data_type = "bm"
            list_spare_parts = json_repository.load_spare_parts_data(data_type)
            spare_part = spare_parts_service.normalize_spare_parts(input("Введите название запчасти: "))
            spare_part_data = spare_parts_service.find_spare_part(list_spare_parts, spare_part)
            print(spare_part_data)


        elif choice == "3":
            break

        else:
            print("Неизвестная команда") 