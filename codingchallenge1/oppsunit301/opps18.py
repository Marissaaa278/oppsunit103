# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:
# 
# import random  # Import the random module to make the computer's choice random

import random
choices = ["rock", "paper", "scissors"]  # List of valid choices

while True:  # Start a loop to repeat the game
    print("\nRock, Paper, Scissors?")  # Ask the player for input
    player_choice = input("Enter your choice: ").lower()  # Convert input to lowercase for consistency

    # Validate player input
    if player_choice not in choices:  # If the input is not one of the valid choices
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue  # Ask for input again

    # Generate computer's choice
    computer_choice = random.choice(choices)  # Randomly select from the choices list
    
    # Show both choices
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()  # Check if the player wants to play again
    if play_again != "yes":  # If the player says anything other than "yes", break the loop and end the game
        print("Thanks for playing!")  # Print a closing message
        break  # Exit the loop and end the game

