import time
import sys
from character import Character
from item import Item
#from wordle import playWordle

def typewriter_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensures the output is displayed immediately
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

# Example usage
typewriter_effect("Hello, this is a typewriter effect!", delay=0.05)

typewriter_effect("Welcome to Walmart Goat Simulator!")

d1 = input("You come up to a field and see a star! Do you want to pick it up? (y/n)")
if d1 == "y":
    star = Item("Star", "A Shiny Star", 10)
    d1a = input ("You picked up the star! Yay! Now you see a dude. Want to talk to him? (y/n)")
    if d1a == "y":
        character = Character("Dude", 100, [], {"Hello": "Hey, I'm a dude!"})
        character.talk_to_player("Hello")

elif d1 == "n":
    typewriter_effect("You cannot stop the voices.", delay=0.06)
    print("""
    """)
    num_repeats = 15

    for _ in range(num_repeats):
        typewriter_effect("Kick the child.", delay=0.04)

    print("""
    """)
    typewriter_effect("You headbutted the child into the stratosphere, leaving the single mother completely devastated...........", delay=0.05)
    typewriter_effect("Excellent Job!!!", delay=0.04)

