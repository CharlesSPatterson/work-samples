class DepthChart:
    """
    A simple depth chart for sports
    """
    
    # a dictionary DS to store the players by position
    players = {}
        
    def addPlayerToDepthChart(self, player, position, depth=None):
        """
        Add a player to a depth chart for a given position (at a specific spot)
        If you are entering two players into the same slot, the last player
        entered gets priority and bumps the existing player down a depth spot.
        If a player is entered without a given depth, they are placed at the
        bottom of the depth chart.
        
        Parameters:
            player: a Player instance of an object
            position: a string representing the position of player
            depth: an integer representing where in the depth chart a player is
        """
        
        # Create a list for a position in the depth chart if it doesn't exist
        if position not in self.players:
            self.players[position] = []
            
        # Spot check for depth (first if depth <= 0, last if None)
        if depth == None:
            depth = len(self.players[position])
        else:
            depth = max(depth,0)
            
        # Place the player in the appropriate position on the depth chart
        self.players[position].insert(depth, player)

    def removePlayerFromDepthChart(self, player, position):
        """
        Remove a player from the depth chart for a position
        
        Parameters:
            player: a Player instance of an object
            position: a string representing the position of player
        """
        try:
            # Gets the index of a player and pops that index(player)
            self.players[position].pop(self.players[position].index(player))
        except KeyError:
            print("Position not found in the depth chart")
        except ValueError:
            print("Player not found in the depth chart")
        except:
            print("An error occured")
    
    def getFullDepthChart(self):
        """
        Prints out all depth chart positions
        """
        for position in self.players:
            
            # Generate a list of player IDs
            order = [player.id for player in self.players[position]]
            
            print(position + ': ' + str(order))
    
    def getPlayersUnderPlayerInDepthChart(self, player, position):
        """
        For a given player, find all players below them on the depth chart
        
        Parameters:
            player: a Player instance of an object
            position: a string representing the position of player
        """
        try:
            # Gets the index of the given player and print players w/ index+1
            index = self.players[position].index(player)
            print(str([player.id for player in self.players[position][index+1:]]))
        except KeyError:
            print("Position not found in the depth chart")
        except ValueError:
            print("Player not found in the depth chart")
        except:
            print("An error occured")