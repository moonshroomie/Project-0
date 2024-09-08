import time
import sys
from character import Character
from item import Item
#from wordle import playWordle

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

# got helped by ChatGPT to make the typewriter effect
def typewriter_effect(text, delay=0.1, color=Colors.RESET):
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()  # Ensures the output is displayed immediately
        time.sleep(delay)
    print()  # Move to the next line after the text is printed # Move to the next line after the text is printed

print()
typewriter_effect("Welcome to Corner Store Simulator!", delay=0.05, color=Colors.CYAN)
print()

typewriter_effect("A man walks into the corner store late at night and approaches you at the counter.... ", delay=0.04, color=Colors.BRIGHT_YELLOW)
d1 = input("Press 'E' to Take the Item: ").lower()
print()
if d1 == "E".lower():
    player = Character("Player", 100, [], {"Hello": "Hey, I'm a dude!"})
    money = Item("Money", "$5.00", 50)
    typewriter_effect("You stole the man's wallet. It had $150 in it. Excellent Job!")
    if d1a == "y":
        character = Character("Dude", 100, [], {"Hello": "Hey, I'm a dude!"})
        character.talk_to_player("Hello")