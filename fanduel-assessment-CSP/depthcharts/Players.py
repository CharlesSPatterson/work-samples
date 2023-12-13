"""
This module allows the instantiation of an athlete via the Player class.
"""

class Player:
    """
    A mutable data structure representing athletes
    
    Attributes:
        id: A unique integer identifying the player
        name: A string repesenting a player's first name
    """
    
    def __init__(self, player_id, name):
        """Inits  player with ID and name"""
        self.id = player_id
        self.name = name
        
    def getId(self):
        return self.player_id
    
    def setId(self, player_id):
        self.player_id = player_id
        
    def getName(self):
        return self.name
    
    def setName(self, first_name, last_name):
        self.first_name = first_name