import json
import os


class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.sid,
            "name": self.name,
            "grade": self.grade
        }


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.students = json.load(f)
        else:
            self.students = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self):
        sid = input("Enter Student ID: ")
        for s in self.students:
            if s["id"] == sid:
                print("❌ ID already exists!")
                return

        name = input("Enter Name: ")
        grade = input("Enter Grade: ")

        student = Student(sid, name, grade)
        self.students.append(student.to_dict())
        self.save_data()
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n--- Student List ---")
        for s in self.students:
            print(f"ID: {s['id']} | Name: {s['name']} | Grade: {s['grade']}")

    def update_student(self):
        sid = input("Enter Student ID to update: ")
        for s in self.students:
            if s["id"] == sid:
                s["name"] = input("Enter new name: ")
                s["grade"] = input("Enter new grade: ")
                self.save_data()
                print("✅ Student updated successfully!")
                return

        print("❌ Student not found!")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")
        for s in self.students:
            if s["id"] == sid:
                self.students.remove(s)
                self.save_data()
                print("✅ Student deleted successfully!")
                return

        print("❌ Student not found!")


def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("👋 Exiting program. Bye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
