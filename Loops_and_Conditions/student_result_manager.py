#🚀 PROJECT 1: Student Result Manager (Lists + Conditions + Loop)
#🎯 What you will build:

#A program that stores student marks and calculates:

#highest score
#lowest score
#average
#pass/fail status


print("Welcome to the Student Result Manager!")

# Step 1: List of marks
student_marks = [85, 92, 78, 90, 88]
students = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5']

# Step 2: Highest and lowest score
highest = max(student_marks)
lowest = min(student_marks)

print("Highest Score:", highest)
print("Lowest Score:", lowest)

# Step 3: Average
average = sum(student_marks) / len(student_marks)
print("Average Score:", average)

# Step 4: Pass/Fail status
print("\nStudent Results:")

for i in range(len(student_marks)):
    mark = student_marks[i]

    if mark >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print(students[i], ":", mark, "-", status)