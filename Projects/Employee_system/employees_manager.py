class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name}.")

    def list_employees(self):
        if len(self.employees) == 0:
            print("No employees.")
            return
        print(f"\nTotal: {len(self.employees)}")
        for i, emp in enumerate(self.employees, 1):
            print(f"  {i}. {emp}")

    def delete_by_age_range(self, min_age, max_age):
        new_list = []
        for emp in self.employees:
            if emp.age < min_age or emp.age > max_age:
                new_list.append(emp)
        deleted = len(self.employees) - len(new_list)
        self.employees = new_list
        print(f"Deleted {deleted} employee(s).")

    def find_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, new_salary):
        emp = self.find_by_name(name)
        if emp is None:
            print(f"{name} not found.")
            return
        emp.salary = new_salary
        print(f"Updated {name}'s salary to {new_salary}.")
