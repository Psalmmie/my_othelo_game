from position import PlayerPosition
from typing import List
from pawn import Pawn

"""
This class is a data container that stores each move of a player
in a list. This class will be responsible for the flipping as a
result of a move.
"""

class Move:

    def __init__(self, position: PlayerPosition, pawn: Pawn):

        self.position = position # Stores where the piece will be placed.

        self.pawn = pawn # Stores which pawn is making the move (black or white).

        self.flipped_position: List[PlayerPosition] = [] #The type hint List[PlayerPosition] means this is a list that should only contain PlayerPosition objects.


# Create a PlayerPosition object (example values)
#pos = PlayerPosition(3, 4)  # adjust args to match your actual class

# Create a Pawn object (example)
#pawn = Pawn(color="black")  # adjust args to match your Pawn class

# Create a Move object
#move_instance = Move(position=pos, pawn=pawn)

# Now you can access its attributes
#print(move_instance.position)
#print(move_instance.pawn)
#print(move_instance.flipped_position)  # starts as empty list
