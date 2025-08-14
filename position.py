
"""
This class gets the player position in the board

It checks if this position is valid wrt to the board size

It then returns TRUE if valid and FALSE otherwise!
"""

class PlayerPosition:

    def __init__(self, row: int, col: int):

        self.row = row

        self.col = col

    """ The following method checks the validity of a player position wrt the board """

    def is_valid(self, board_size: int = 8) -> bool:

        return 0 <= self.row < board_size and 0 <= self.col < board_size

    """ To make the object of this class behave naturally when compared and also have a good display, 
    we will overwrite the Python's special methods '__eq__' and '__str__' """

    def __eq__(self, other) -> bool:

        return isinstance(other, PlayerPosition) and self.row == other.row and self.col == other.col


    def __str__(self) -> str:

        return f"({self.row}, {self.col})"


#position1 = PlayerPosition(2,3)

#position2 = PlayerPosition(0,7)

#print(position1.is_valid())

#print(position1 == position2)

#print(position1)
