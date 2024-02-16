
class Employee:
    def __init__(self, name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

    def __str__(self):
        return f"{self.name} - ID: {self.employee_id}"