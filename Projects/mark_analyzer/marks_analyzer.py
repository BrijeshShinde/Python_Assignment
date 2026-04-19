class StudentMarksAnalyzer:
    def __init__(self):
        self.students = {}   # name -> marks

    def add_student(self):
        name = input("Student name: ").strip()
        if name == "":
            print("Name cannot be empty.")
            return
        if name in self.students:
            print(f"'{name}' already exists.")
            return
        try:
            marks = int(input("Marks: "))
        except ValueError:
            print("Marks must be an integer.")
            return
        self.students[name] = marks
        print(f"Added {name} with marks {marks}.")

    def remove_student(self):
        name = input("Student name to remove: ").strip()
        if name in self.students:
            del self.students[name]
            print(f"Removed {name}.")
        else:
            print(f"{name} not found.")

    def list_students(self):
        if len(self.students) == 0:
            print("No students yet.")
            return
        print(f"\nTotal: {len(self.students)}")
        for name, marks in self.students.items():
            print(f"  {name:<20} {marks}")

    def show_report(self):
        if len(self.students) == 0:
            print("No students to analyze.")
            return

        total_students = len(self.students)
        all_marks = list(self.students.values())
        average = sum(all_marks) / total_students
        highest = max(all_marks)
        lowest = min(all_marks)

        top_students = [name for name, m in self.students.items() if m == highest]
        low_students = [name for name, m in self.students.items() if m == lowest]

        print("\n" + "=" * 40)
        print("      STUDENT MARKS REPORT")
        print("=" * 40)
        print(f"Total students : {total_students}")
        print(f"Average marks  : {average:.2f}")
        print(f"Highest marks  : {highest}  ->  {', '.join(top_students)}")
        print(f"Lowest marks   : {lowest}  ->  {', '.join(low_students)}")
        print("=" * 40)

    def run(self):
        while True:
            print("\n--- Student Marks Analyzer ---")
            print("1. Add student")
            print("2. Remove student")
            print("3. List all students")
            print("4. Show report")
            print("0. Exit")

            choice = input("Choose: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.show_report()
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = StudentMarksAnalyzer()
    app.run()
