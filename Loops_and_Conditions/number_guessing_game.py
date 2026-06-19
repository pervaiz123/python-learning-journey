#Build a Number Guessing Game:
#1. Use def main() to start the program
#2. Pick a secret number (you can hardcode it: secret = 7)
#3. Use while True to keep asking for guesses
#4. Use try/except to handle if user types "abc" instead of a number
#5. Use if/else to say "Too high!", "Too low!", or "Correct!"
#6. Use break when they guess correctly
#7. Use int() to convert their input
#8. At the bottom, use: if __name__ == "__main__": main()

def main():
    secret = 7

    while True:
        try:
            guess = int(input("Enter the guessing number: "))

        except ValueError:
            print("Number only!")
            continue

        if guess < secret:
            print("Too Low")

        elif guess > secret:
            print("Too High")

        else:
            print("Correct Number")
            break


if __name__ == "__main__":
    main()