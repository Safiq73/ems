from employee import Employee
from company import Company



def print_menu():
    print()
    print("Employee Management System Menu:")
    print("1. Add Employee to Department")
    print("2. Remove Employee from Department")
    print("3. List Employees in Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. List Departments")
    print("7. Exit")

def main():
    company = Company()
    company.load_data()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department name: ")

            if department in company.departments:
                employee = Employee(name, employee_id, title, department)
                company.departments[department].add_employee(employee)
            else:
                print("Department does not exist.")

        elif choice == "2":
            department = input("Enter department name: ")
            employee_id = input("Enter employee ID to remove: ")

            if department in company.departments:
                company.departments[department].remove_employee(employee_id)
            else:
                print("Department does not exist.")

        elif choice == "3":
            department = input("Enter department name: ")
            if department in company.departments:
                print(f"Employees in {department}:")
                company.departments[department].list_employees()
            else:
                print("Department does not exist.")

        elif choice == "4":
            department_name = input("Enter department name to add: ")
            company.add_department(department_name)

        elif choice == "5":
            department_name = input("Enter department name to remove: ")
            company.remove_department(department_name)

        elif choice == "6":
            print("Departments:")
            company.display_departments()

        elif choice == "7":
            company.save_data()
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
