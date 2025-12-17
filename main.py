import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")

def search_student():
    roll_no = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll_no:
            print("\nStudent Found")
            print(f"Name: {s['name']} | Roll: {s['roll']} | Marks: {s['marks']}")
            return

    print("Student not found")
        
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']} | Roll: {s['roll']} | Marks: {s['marks']}")

students = load_students()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Program exited.")
        break
    else:

        print("Invalid choice!")

