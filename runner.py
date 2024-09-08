import time
import sys
from character import Character
from item import Item

class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    RESET = '\033[0m'  # Resets the color to default

# Typewriter effect function
def typewriter_effect(text, delay=0.1, color=Colors.RESET):
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()  # Ensures the output is displayed immediately
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

# Initial text introduction
print()
typewriter_effect("Welcome to Corner Store Simulator!", delay=0.05, color=Colors.CYAN)
print()

typewriter_effect("A man walks into the corner store late at night and approaches you at the counter....", delay=0.04, color=Colors.BRIGHT_YELLOW)
print()

# Character creation with dialogue
player = Character("Man", 100, [], {
    "Hello": ("NPC: Hey, you guys got any lighters here?", Character.Colors.GREEN, 0.04),
    "No": ("YOU: No, but we may have some in the back. I'll go check.", Character.Colors.BLUE, 0.04),
    "Give": ("YOU: I found a pack in the back.", Character.Colors.BLUE, 0.04),
    "Goodbye": ("NPC: Thank you, have a good night!", Character.Colors.GREEN, 0.04)
})
in_conversation = False

# Game loop for continuous interaction
while True:
    if not in_conversation:
        # Start the conversation
        d1 = input("Press 'E' to greet them or 'Q' to end the conversation: ").lower()

        if d1 == "e":
            # Player starts talking to the character
            player.talk_to_player("Hello")
            in_conversation = True  # Now the conversation starts, waiting for player reply
        elif d1 == "q":
            # Exit the game
            typewriter_effect("Goodbye!", delay=0.05, color=Colors.RED)
            break
        else:
            print("Invalid input. Please press 'E' or 'Q'.")
        print()
    
    in_conversation = False
    found_lighters = False

    # Game loop for continuous interaction
    while True:
        if not in_conversation:
            d2 = input("Press 'E' to reply or 'Q' to end: ").lower()

            if d2 == "e":
                player.talk_to_player("No")  # Player's response: "No, but we may have some in the back"
                print()
                typewriter_effect("You walk into the backroom but don't know where to look. Left or Right?", delay=0.04, color=Character.Colors.BRIGHT_YELLOW)
                
                while not found_lighters:
                    d2 = input("Press 'L' for left or 'R' for right: ").lower()
                    if d2 == "l":
                        # Create a lighter item and add it to the player's inventory
                        lighters = Item("Lighter", "A pack of lighters", 0)
                        player.inventory.append(lighters)
                        typewriter_effect("You find a pack of lighters next to the rat's nest in the corner and pick them up.", delay=0.04, color=Character.Colors.BRIGHT_YELLOW)
                        found_lighters = True
                    elif d2 == "r":
                        typewriter_effect("You don't find any lighters and turn back.", delay=0.04, color=Character.Colors.BRIGHT_YELLOW)
                        print()
                        typewriter_effect("You're back in the backroom. Left or Right?", delay=0.04, color=Character.Colors.BRIGHT_YELLOW)
                    else:
                        print("Invalid response. Press 'L' for left or 'R' for right.")

            elif d2 == "q":
                typewriter_effect("Goodbye!", delay=0.05, color=Character.Colors.RED)
                break
            else:
                print("Invalid response. Press 'E' to reply 'No' or 'Q' to quit.")

        print()
        if found_lighters:
            d3 = input("Press 'G' to give the lighters to the man: ").lower()

            if d3 == "g":
                if lighters in player.inventory:
                    player.inventory.remove(lighters)  # Remove the lighters from the player's inventory
                    player.talk_to_player("Give")
                    typewriter_effect("You gave the lighters to the man. He gives you his thanks and pays.", delay=0.04, color=Colors.YELLOW)
                    print()
                    d3a = input("Press 'E' to say goodbye: ").lower()
                    if d3a == "e":
                        player.talk_to_player("Goodbye") 
                        typewriter_effect("The man walks out of the store.", delay=0.04, color=Colors.YELLOW)   
                else:
                    typewriter_effect("You don't have any lighters.", delay=0.04, color=Character.Colors.RED)
            elif d3 == "q":
                typewriter_effect("Goodbye!", delay=0.05, color=Character.Colors.RED)
                break
            else:
                print("Invalid Input. Press 'G' to give the lighters or 'Q' to quit.")
    break