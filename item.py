
class Item:
    """
        Represents an item that can be used by a player to increase their health.
        
        Args:
            name (str): The name of the item.
            description (str): A description of the item.
            points (int): The number of health points the item will restore when used.
        
        Methods:
            use_item(player: Player) -> None:
                Increases the player's health by the item's points value, and sets the item's points to 0.
        """
    def __init__(self, name, description, points):
            self.name = name
            self.description = description
            self.points = points
            
    def use_item(self, player):
            player.health += self.points
            self.points = 0


