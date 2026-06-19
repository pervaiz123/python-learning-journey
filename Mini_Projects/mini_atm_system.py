#Mini ATM System
#Requirements:
#Start with:
#balance = 1000
#Menu:
#1. Check Balance
#2. Deposit
#3. Withdraw
#4. Exit

pin = int(input("Enter your Pin"))
balance = 1000

print("Welcome to the MinI Atm Machine")
print("Choose Your Account Type")
options =["Current, Savings, Bussiness"]
for i, option in enumerate(options, start=1):
    print(f"{i}. {option}")



print("Menu")
print("1:Check Balance")
print("2:Deposit")
print("3:Withdraw")
print("4:Funds Transfer")
print("5:Exit")

choice =int(input("Enter your choice"))
if choice == 1:
    print("You have selected to Check Balance")
    print("print the balance", balance)
elif choice == 2:
        deposit = int(input("Enter the Amount to Deposit"))
        print("balance Depsoit Successfully")
        new_balance = [deposit]
        balance += deposit
        print("Balance:", balance)
        
elif choice == 3:
    withdraw = int(input("Enter the Amount to Withdraw"))
    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawn Successfully")
        print("Balance:", balance)
    else:
        print("Insufficient funds")
elif choice == 4:
    funds_transfer = int(input("Enter the Account Number"))
    amount = int(input("Enter the Amount to Transfer"))
    print("Payment Transfer Successfully")
elif choice == 5:
    print("Thank you for Using this ATM")
    exit()
            
                