from employee import Employee
from employees_manager import EmployeesManager


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def add_employee(self):
        name = input("Name: ")
        age = int(input("Age: "))
        salary = float(input("Salary: "))
        emp = Employee(name, age, salary)
        self.manager.add_employee(emp)

    def list_employees(self):
        self.manager.list_employees()

    def delete_by_age_range(self):
        min_age = int(input("Min age: "))
        max_age = int(input("Max age: "))
        self.manager.delete_by_age_range(min_age, max_age)

    def find_employee(self):
        name = input("Name: ")
        emp = self.manager.find_by_name(name)
        if emp:
            print(emp)
        else:
            print(f"{name} not found.")

    def update_salary(self):
        name = input("Name: ")
        new_salary = float(input("New salary: "))
        self.manager.update_salary_by_name(name, new_salary)

    def run(self):
        while True:
            print("\n--- Employees System ---")
            print("1. Add employee")
            print("2. List employees")
            print("3. Delete by age range")
            print("4. Find employee")
            print("5. Update salary")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.list_employees()
            elif choice == "3":
                self.delete_by_age_range()
            elif choice == "4":
                self.find_employee()
            elif choice == "5":
                self.update_salary()
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = FrontendManager()
    app.run()
