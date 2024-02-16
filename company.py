from department import Department
from employee import Employee
import json


class Company:
    def __init__(self):
        self.departments = {}
        self.filename = "data.json"

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
        else:
            print("Department already exists.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
        else:
            print("Department does not exist.")

    def display_departments(self):
        for department in self.departments.values():
            print(department.name)

    def save_data(self, ):
        with open(self.filename, 'w') as f:
            json.dump(self.departments, f, default=lambda o: o.__dict__, indent=4)

    def load_data(self,):
        with open(self.filename, 'r+') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                return
            print(data)
            for department_name in data:
                department = Department(department_name)
                for employee_data in data.get(department_name, {}).get("employees", {}).values():
                    employee = Employee(**employee_data)
                    department.add_employee(employee)
                self.departments[department_name] = department