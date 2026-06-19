#Create a lucky draw game where the user keeps guessing a randomly selected lucky number.
#1️⃣ Import Random
#2️⃣ Create main()
#3️⃣ Generate Lucky Number
#Generate a random number between:
#4️⃣ Give User 5 Attempts
#5️⃣ Use try/except
#If user enters:
#Program should NOT crash.
#Show:
#Please enter numbers only
#6️⃣ Compare Guess
#If guess is smaller:
#7️⃣ Show Remaining Attempts
#Example:
#8️⃣ If User Loses
#When attempts become 0:
#Show:
#Game Over
#and reveal the lucky number.
#Example:
# #The lucky number was: 13

def main():
    import random
    lucky_number = random.randint(1, 10)
    attempts = 5

    while attempts > 0:
        try:
            guess = int(input("Enter the lucky number: "))
        except ValueError:
            print("Please enter numbers only")
            attempts -= 1
            print("Attempts left", attempts)
            continue

        if guess == lucky_number:
            print("You WON THE GAME")
            break
        elif guess < lucky_number:
            print("Too low")
        else:
            print("Too high")

        attempts -= 1
        if attempts > 0:
            print("Attempts left", attempts)

    if attempts == 0:
        print("Game Over")
        print("The lucky number was:", lucky_number)

        

if __name__ == "__main__":
    main()