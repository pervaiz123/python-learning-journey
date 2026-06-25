import csv


def add_expense():
    name = input("Enter Expense Name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Amount must be a number.")
        return

    with open("expenses.csv" "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount])

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            found = False

            print("\n===== EXPENSE LIST =====")

            for row in reader:
                if row:
                    print(f"{row[0]} - {row[1]}")
                    found = True

            if not found:
                print("No expenses found.")

            print()

    except FileNotFoundError:
        print("No expense records available.\n")


def total_spending():
    amounts = []

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    amounts.append(float(row[1]))

        if len(amounts) == 0:
            print("No expenses available.\n")
            return

        total = sum(amounts)

        print("\nTotal Expenses:", total)
        print()

    except FileNotFoundError:
        print("No expense records available.\n")


def search_expense():
    search_name = input("Enter Expense Name: ").strip()

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0].lower() == search_name.lower():
                    print("\nExpense Found")
                    print("Name:", row[0])
                    print("Amount:", row[1])
                    print()
                    return

            print("Expense not found.\n")

    except FileNotFoundError:
        print("No expense records available.\n")


def main():
    while True:

        print("===== EXPENSE TRACKER SYSTEM =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Search Expense")
        print("5. Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            total_spending()

        elif choice == 4:
            search_expense()

        elif choice == 5:
            print("Thank you for using Expense Tracker.")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()