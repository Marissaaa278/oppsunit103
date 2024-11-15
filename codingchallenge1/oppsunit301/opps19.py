# List of valid yes/no responses
yes_no = ["yes", "no"]

# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")

# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n").lower()
    if response == "yes":
        print("You head into the forest. You hear crows cawing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()  # Ends the game
    else:
        print("I didn't understand that.\n")

response = ""
while response not in yes_no:
    response = input("You see a white rabbit with a pocket watch and waistcoat. Would you like to follow it?\nyes/no\n").lower()
    if response == "yes":
        print("You follow it down a rabbit hole and land inside a room with a table.")
    elif response == "no":
        print("You remain on the edge of the forest.")
        quit()  # Ends the game
    else:
        print("I didn't understand that. Choose again.\n")

response = ""
while response not in yes_no:
    response = input("You find a tiny key to a tiny door. How will you fit? You find a potion that says 'Drink me'. Do you take it?\nyes/no\n").lower()
    if response == "yes":
        print("You shrink down and walk through the door to find yourself among various animals and birds.")
    elif response == "no":
        print("You remain stuck in the room.")
        quit()  # Ends the game
    else:
        print("I didn't understand that. Choose again.\n")

# Direction choice (left or right)
directions = ["left", "right"]  # Valid directions

response = ""
while response not in directions:
    response = input("As you follow the rabbit, you find a fork in the road. Which path are you taking?\nleft/right\n").lower()
    if response == "left":
        print("You take the left path and find a cat sitting upon a tree.\n")
    elif response == "right":
        print("You take the right path and find a caterpillar sitting on a mushroom.")
        quit()  # Ends the game
    else:
        print("I didn't understand that. Choose again.\n")

# Character encounter: cat or caterpillar
characters = ["cat", "caterpillar"]

response = ""
while response not in characters:
    response = input("You lost the rabbit. Who do you speak to first?\ncat/caterpillar\n").lower()

    if response == "cat":
        print("The cat shows you the way to the white rabbit.")
    elif response == "caterpillar":
        print("The caterpillar asks you too many questions, distracting you from your mission. He asks if you'd like a bite of his mushroom.\nyes/no\n")
        
        # Ask for a new response to the caterpillar's question
        mushroom_response = input().lower()
        
        if mushroom_response == "no":
            print("You walk away from the caterpillar.")
        elif mushroom_response == "yes":
            print("You eat the mushroom and die. Sorry, game over.")
            quit()  # Ends the game
        else:
            print("I didn't understand that. Choose 'yes' or 'no'.")
            continue  # Repeats the caterpillar question
    else:
        print("I didn't understand that. Choose again.\n")
