from patient import Patient
from specialization import Specialization


class OperationsManager:
    def __init__(self):
        self.specializations = {}

    def add_specialization(self):
        name = input("Specialization name: ")
        capacity = int(input("Capacity: "))
        self.specializations[name] = Specialization(name, capacity)
        print(f"Created {name}.")

    def add_patient(self):
        spec_name = input("Specialization name: ")
        if spec_name not in self.specializations:
            print("Specialization not found.")
            return
        name = input("Patient name: ")
        status = int(input("Status (0=Normal, 1=Urgent, 2=Super-Urgent): "))
        patient = Patient(name, status)
        self.specializations[spec_name].add_patient(patient)

    def list_patients(self):
        spec_name = input("Specialization name: ")
        if spec_name in self.specializations:
            self.specializations[spec_name].list_patients()
        else:
            print("Specialization not found.")

    def get_next_patient(self):
        spec_name = input("Specialization name: ")
        if spec_name in self.specializations:
            self.specializations[spec_name].get_next_patient()
        else:
            print("Specialization not found.")

    def remove_patient(self):
        spec_name = input("Specialization name: ")
        if spec_name not in self.specializations:
            print("Specialization not found.")
            return
        name = input("Patient name to remove: ")
        self.specializations[spec_name].remove_by_name(name)

    def run(self):
        while True:
            print("\n--- Hospital Queue ---")
            print("1. Add specialization")
            print("2. Add patient")
            print("3. List patients")
            print("4. Get next patient")
            print("5. Remove patient")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add_specialization()
            elif choice == "2":
                self.add_patient()
            elif choice == "3":
                self.list_patients()
            elif choice == "4":
                self.get_next_patient()
            elif choice == "5":
                self.remove_patient()
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    manager = OperationsManager()
    manager.run()
