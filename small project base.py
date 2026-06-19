name = input("Enter your name")
print("hello," + name.capitalize())

print("Welcome to the ATM MACHINE SYSTEM")

print("Choose  your Account type")
options = ["Savings", "Current", "Business"]       
for i, option in enumerate(options, start=1):
    print(f"{i}. {option}")

pin = int(input("Enter your 4-digit PIN: "))



print("===== MENU =====")

print("1. Funds Transfer")
print("2. Check Balance")       
print("3. Pay Bills")
print("4. Withdraw Cash")
print("5. chose amount to withdraw") 
print("6. Exit")

choice = int(input("input your choice:"))
if choice == 1:
    print("You have chosen Funds Transfer")
    choice = int(input("Enter the amount you want to transfer: "))
    print("Funds Transfer successful")
elif choice == 2:  
    print("You have chosen Check Balance")
    print("Your balance is $1000")
elif choice == 3:
    print("You have chosen Pay Bills")
    choice = int(input("Enter the amount you want to pay: "))
    print("Bill payment successful")
elif choice == 4:
    print("You have chosen Withdraw Cash")
    choice = int(input("Enter the amount you want to withdraw: "))
    print("Cash withdrawal successful")
elif choice == 5:
    print("You have chosen chose amount to withdraw")
    choice = int(input("Enter the amount you want to withdraw: "))
    print("Cash withdrawal successful")
elif choice == 6:
    print("Thank you for using the ATM MACHINE SYSTEM. Goodbye!")