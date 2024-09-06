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

print()
typewriter_effect("Welcome to the Ultimate Goat Experience!", delay=0.04)
print()

typewriter_effect("You see a man pull out his wallet to pay for his food at a hot dog stand, do you intercept and take it?", delay=0.03)
d1 = input("Y/N: ").lower()
print()
if d1 == "y":
    wallet = Item("Wallet", "Leather Wallet", 150)
    character.receive_item("Wallet")
    typewriter_effect("You stole the man's wallet. It had $150 in it. Excellent Job!")
    if d1a == "y":
        character = Character("Dude", 100, [], {"Hello": "Hey, I'm a dude!"})
        character.talk_to_player("Hello")