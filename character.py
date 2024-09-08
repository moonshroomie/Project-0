class Character:
    """
    Represents a character in the game.
    
    The `Character` class encapsulates the properties and behaviors of a character in the game, such as their name, health, inventory, and dialogue.
    
    Attributes:
        name (str): The name of the character.
        health (int): The current health of the character.
        inventory (list): The items in the character's inventory.
        dialogue (dict): A dictionary mapping player messages to the character's responses     
    
    Methods:
        talk_to_player(player_msg: str) -> None:  
            Prints the character's response to the given player message, if it exists in the character's dialogue.
        receive_item(item: Any) -> None:
            Adds the given item to the character's inventory.
    """
class Character:
    def __init__(self, name, health, inventory, dialogue):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.dialogue = dialogue

    def talk_to_player(self, player_msg):
        if player_msg in self.dialogue:
            print(self.dialogue[player_msg])
        else:
            print("I don't know what to say.")

    def receive_item(self, item):
        self.inventory.append(item)