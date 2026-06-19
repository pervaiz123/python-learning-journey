#

#Create a Python program that shows this menu:

#===== MENU =====

#1. Add Student
#2. Show Students
#3. Search Student
#4. Count Students
#5. Delete Student
#6. Ask for a student name:
    
#7. Exit
#When the user selects option 1, the program should ask for the student name and add it to a list.
#When the user selects option 2, the program should display all the student names in the list.
#When the user selects option 3, the program should ask for a student name and check if it exists in the list. If it does, it should display "Student found", otherwise it should display "Student not found".
#When the user selects option 4, the program should display the total number of students in
#the list.
#When the user selects option 5, the program should ask for a student name and remove it from the list if it exists. If it does not exist, it should display "Student not found".
#When the user selects option 6, the program should ask for a student name and display "Hello, [student name]!".
#When the user selects option 7, the program should exit.  
 
students = ['ahmed', 'ali', 'sara', 'perviaz', 'imtiaz']
while True:
    print("===== MENU =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Count Students")
    print("5. Delete Student")
    print("6. Ask for a student name:")
    print("7. Exit")
    
    choice = input ("Enter your choice:")
    if choice == "1":
        name = input ("Enter student name:")
        students.append(name)
    elif choice == "2":
        print("students")
    elif choice == "3":
        name = input ("Enter student name to search:")
        if name in students:
            print("Student found")
        else: print("Student not found")
    elif choice == "4":
        print("Total number of students:", len(students))
    elif choice == "5":
        name = input ("Enter student name to delete:")
        if name in students:
            students.remove(name)
            print("Student deleted")
        else: print("Student not found")
    elif choice == "6":
        name = input ("Enter student name:")
        print("Hello, " + name + "!")
         
    