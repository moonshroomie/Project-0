from character import Character
from item import Item
#from wordle import playWordle

print("Welcome to Walmart Goat Simulator!")
print(""
      "")
d1 = input("You see a single mother walking down the sidewalk with her 3 year-old son. Do you headbutt her son into the stratosphere? (y/n)")
if d1 == "y":
    child = Item("Child", "3 year-old", 10)
    print("You headbutted the child into the stratosphere! Excellent work!")
    d1a = input ("You picked up the star! Yay! Now you see a dude. Want to talk to him? (y/n)")
    if d1a == "y":
        character = Character("Dude", 100, [], {"Hello": "Hey, I'm a dude!"})
        character.talk_to_player("Hello")
