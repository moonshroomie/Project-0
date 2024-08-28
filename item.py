class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.points = points 

    def use_item(self, player):
        player.health += self.points
        self.points = 0
