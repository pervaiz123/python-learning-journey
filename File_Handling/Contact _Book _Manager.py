import csv


def add_contact():
    name = input("Enter Contact Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    number = input("Enter Phone Number: ").strip()

    with open("contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, number])

    print("Contact added successfully!\n")


def view_contacts():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)

            found = False

            print("\n===== CONTACT LIST =====")

            for row in reader:
                if row:
                    print(f"{row[0]} - {row[1]}")
                    found = True

            if not found:
                print("No contacts found.")

            print()

    except FileNotFoundError:
        print("No contacts available.\n")


def search_contact():
    search_name = input("Enter Contact Name: ").strip()

    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0].lower() == search_name.lower():
                    print("\nContact Found")
                    print("Name:", row[0])
                    print("Phone:", row[1])
                    print()
                    return

            print("Contact not found.\n")

    except FileNotFoundError:
        print("No contacts available.\n")


def delete_contact():
    delete_name = input("Enter Contact Name to Delete: ").strip()

    contacts = []
    found = False

    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0].lower() == delete_name.lower():
                    found = True
                else:
                    contacts.append(row)

        with open("contacts.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        if found:
            print("Contact deleted successfully.\n")
        else:
            print("Contact not found.\n")

    except FileNotFoundError:
        print("No contacts available.\n")


def main():

    while True:

        print("===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if choice == 1:
            add_contact()

        elif choice == 2:
            view_contacts()

        elif choice == 3:
            search_contact()

        elif choice == 4:
            delete_contact()

        elif choice == 5:
            print("Thank you for using Contact Book.")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()