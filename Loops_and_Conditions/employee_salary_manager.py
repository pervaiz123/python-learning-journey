
#Project 4: Employee Salary Manager

#Requirements:


#Prints every employee with salary
#Finds lowest salary
#Finds average salary
#Gives a 10% bonus to everyone
#Prints updated salaries
#Counts employees earning above 60,000


employees = ["Ali", "Sara", "John", "Ahmed"]
salaries = [50000, 70000, 45000, 90000]


#Prints every employee with salary
for i in range(len(employees)):
    print(employees[i],(salaries[i]))

highest =max(salaries)
lowest =min(salaries)
Average =sum(salaries) /len(salaries)

print("Highest salaries",highest)
print("lowest salaries",lowest)
print("Average salaries",Average)
new_salaries = [salary * 1.10 for salary in salaries]

print("updated Salaries after Addition")
for i in range(len(employees)):
    print(employees[i],":" ,(new_salaries[i]))

count =sum (1 for s in new_salaries above>60000)
print("/n Employees Earning above 60000",count)











# Count employees earning above 60,000 (original salaries)