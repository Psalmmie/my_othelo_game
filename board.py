
from typing import List, Optional
from pawn import Pawn
from color import Color
from copy import deepcopy
from position import PlayerPosition 

class Board:

    BOARD_SIZE = 8 # The Othelo board is 8x8 

    """ This method creates the othello board """

    def __init__(self):

        self.__grid: List[List[Optional[Pawn]]] = [

                [None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)
                
                ]

    """ This method returns the borad with its grids for valid pawn position """
    """ It returns None if the pawn move is invalid"""

    def get_cell(self, position: PlayerPosition) -> Optional[Pawn]:

        if position.is_valid():

            return self.__grid[position.row][position.col]
        
        else:

            return None

    """ This method returns the board with pawn placed at a given color at a given position """
    """ When a player makes a move, this is how we update the board state. """

    def set_cell(self, position: PlayerPosition, pawn: Pawn) -> None:

        if position.is_valid():

            self.__grid[position.row][position.col] = pawn

    """ This method returns a list of all possible coordinates on the board """
    """ This is needed to check all cells """

    def get_all_positions(self) -> List[PlayerPosition]:

        positions = [] # Empty list to store all the positions

        for row in range(self.BOARD_SIZE):

            for col in range(self.BOARD_SIZE):

                positions.append(PlayerPosition(row, col))

        return positions


    """ The following method checks if there are no empty cells left """
    """ It is needed because the game ends when the board is full """

    def is_full(self) -> bool:

        for row in self.__grid:

            for cell in row:

                if cell is None:

                    return False
        return True

    
    """ We need to track the score of the game at each point """
    """ We can create a count pawn method """

    def count_pawns(self, color: Color) -> int:

        count = 0

        for row in self.__grid:

            for cell in row:

                if cell is not None and cell.color == color:

                    count += 1
        
        return count


    """ To simulate possible moves without altering the real board, we can create a copy of the board"""
    def copy(self) -> "Board":

        new_board = Board()

        new_board.__grid = deepcopy(self.__grid)

        return new_board



#pos1 = PlayerPosition(3,3)
#pos2 = PlayerPosition(0,8)
#pawn_black = Pawn(Color.BLACK)
#ipawn_white = Pawn(Color.WHITE)

#board = Board()
#board.set_cell(pos1, pawn_black)
#board.set_cell(pos2, pawn_white)

#print(board.get_cell(pos1))
#print(board.get_cell(pos2))
#print(board.count_pawns(Color.BLACK))
#print(board.count_pawns(Color.WHITE))
