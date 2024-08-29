from character import Character
from item import Item
from wordle import playWordle

print("Welcome to the Game!")

d1 = input("You come up to a field and see a star! Do you want to pick it up? (y/n)")
if d1 == "y":
    star = Item("Star", "A Shiny Star", 10)
    d1a = input ("You picked up the star! Yay! Now you see a dude. Want to talk to him? (y/n)")
    if d1a == "y":
        character = Character("Dude", 100, [], {"Hello": "Hey, I'm a dude!"})
        character.talk_to_player("Hello")
