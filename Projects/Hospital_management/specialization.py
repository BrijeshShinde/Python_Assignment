class Specialization:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
    def is_full(self):
        return len(self.patients) >= self.capacity

    def add_patient(self, patient):
        if self.is_full():
            print(f"{self.name} queue is full.")
            return
        self.patients.append(patient)
        self.patients.sort(key=lambda p: p.status, reverse=True)
        print(f"Added {patient.name} to {self.name}.")

    def get_next_patient(self):
        if len(self.patients) == 0:
            print(f"No patients in {self.name}.")
            return
        patient = self.patients.pop(0)
        print(f"Next patient: {patient}")

    def remove_by_name(self, name):
        for patient in self.patients:
            if patient.name == name:
                self.patients.remove(patient)
                print(f"Removed {name}.")
                return
        print(f"{name} not found.")

    def list_patients(self):
        if len(self.patients) == 0:
            print(f"{self.name} is empty.")
            return
        print(f"\n{self.name} ({len(self.patients)}/{self.capacity}):")
        for i, patient in enumerate(self.patients, 1):
            print(f"  {i}. {patient}")
