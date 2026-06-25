#Project: Student Record Management System v1
#Build a program that allows a user to manage student recordsand save them permanently in a CSV file.
#Program Requirements
#When program starts:
#===== STUDENT RECORD MANAGEMENT SYSTEM =====
#Show menu:
#1. Add Student
#2. View Students
#3. Search Student
#4. Show Statistics
#5. Exit
#Requirements: Name cannot be empty
#Marks must be a number
#Use try/except
#Save data to:
#students.csv

import csv


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Marks must be a number!")
        return

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, marks])

    print("Student added successfully!\n")


def view_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            print("\n--- STUDENT LIST ---")

            found = False

            for row in reader:
                if row:
                    print(f"{row[0]} - {row[1]}")
                    found = True

            if not found:
                print("No students found.")

    except FileNotFoundError:
        print("No student records found.")

    print()


def search_student():
    search_name = input("Enter student name to search: ").strip()

    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0].lower() == search_name.lower():
                    print("\nStudent Found")
                    print("Name:", row[0])
                    print("Marks:", row[1])
                    print()
                    return

            print("Student not found.\n")

    except FileNotFoundError:
        print("No student records found.\n")


def show_statistics():
    marks_list = []

    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    marks_list.append(int(row[1]))

        if len(marks_list) == 0:
            print("No records available.\n")
            return

        highest = max(marks_list)
        lowest = min(marks_list)
        average = sum(marks_list) / len(marks_list)

        passed = 0
        failed = 0

        for mark in marks_list:
            if mark >= 50:
                passed += 1
            else:
                failed += 1

        print("\n--- STATISTICS ---")
        print("Highest Marks:", highest)
        print("Lowest Marks:", lowest)
        print("Average Marks:", round(average, 2))
        print("Total Students:", len(marks_list))
        print("Students Passed:", passed)
        print("Students Failed:", failed)
        print()

    except FileNotFoundError:
        print("No student records found.\n")


def main():

    while True:

        print("===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Show Statistics")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            show_statistics()

        elif choice == 5:
            print("Thank you for using Student Record Management System!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 2fcaa80 (Added Expense Tracker and Contact Book Manager projects)
