# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?

import random

answer = random.randint(1, 20)
numberofguesses = 0

print("Guess a number between 1 and 20.")

while True:
    number = int(input("Your guess: "))
    numberofguesses += 1

    if numberofguesses > 5:
        print(f"Out of guesses! The number was {answer}.")
        break

    if number == answer:
        print(f"Correct! The answer was {answer}. It took you {numberofguesses} guess(es)!")
        break
    elif number > answer:
        print("Too high! The number needs to be lower!")
    elif number < answer:
        print("Too low! The number needs to be higher!")
    else:
        print("Invalid input. Please try again.")

# Optional: If you want to ask for input again after invalid input
