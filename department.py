from employee import Employee

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = {}

    def add_employee(self, employee:Employee):
        self.employees[employee.employee_id] = employee

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return
        print("Employee not found in this department.")

    def list_employees(self):
        for employee in self.employees.values():
            print(employee)
