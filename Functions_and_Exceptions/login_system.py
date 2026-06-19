# LOGIN SYSTEM (3 ATTEMPTS)

# User has only 3 chances to enter correct password.

# 🧠 REQUIREMENTS
# Use def main()
# Set a correct password (hardcoded)
# Allow only 3 attempts
# Use while loop
# Use try/except (for input safety practice)
# Use break when login is correct
# Show messages:
# "Access Granted"
# "Wrong Password"
# "Attempts left"

def main():
    correct_password = 1234
    attempts = 3
    while attempts > 0:
        try:
            password = int(input("Enter the password: "))
            if password == correct_password:
                print("Access Granted")
                break
            attempts -= 1
            print("Wrong Password")
            if attempts > 0:
                print("Attempts left", attempts)
            else:
                print("Account Locked")
        except ValueError:
            print("Invalid input. Please enter a number.")
            attempts -= 1
            if attempts > 0:
                print("Attempts left", attempts)
            else:
                print("Account Locked")


if __name__ == "__main__":
    main()
