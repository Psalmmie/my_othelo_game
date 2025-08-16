
"""
This class gets the player position in the board

It checks if this position is valid wrt to the board size

It then returns TRUE if valid and FALSE otherwise!
"""

class PlayerPosition:

    def __init__(self, row: int, col: int):

        self.row = row

        self.col = col


    def __hash__(self):
        return hash((self.row, self.col))


    def __repr__(self):
        return f"PlayerPosition(row={self.row}, col={self.col})"


    """ The following method checks the validity of a player position wrt the board """

    def is_valid(self, board_size: int = 8) -> bool:

        return 0 <= self.row < board_size and 0 <= self.col < board_size

    """ To make the object of this class behave naturally when compared and also have a good display, 
    we will overwrite the Python's special methods '__eq__' and '__str__' """

    def __eq__(self, other) -> bool:

        return isinstance(other, PlayerPosition) and self.row == other.row and self.col == other.col


    def __str__(self) -> str:

        return f"({self.row}, {self.col})"


#position1 = PlayerPosition(3,3)

#position2 = PlayerPosition(8,0)

#print(position2.is_valid())

#print(position1 == position2)

#print(position1)
