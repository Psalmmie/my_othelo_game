from board import Board
from pawn import Pawn
from color import Color
from position import PlayerPosition
from typing import List, Optional
from player_move import Move

""" This class set the rules for the Othello game. """

class GameRules:

    Board_size = 8

    # The directions to be checked around a particular player

    Directions = [

            (1, 0), (-1, 0),

            (0, 1), (0, -1),

            (1, 1), (-1, -1),

            (1, -1), (-1, 1)

    ]

    """ Not all moves around a player are valid. Therefore, we will return all valid moves """
    """using the following methods"""

    @staticmethod
    def get_valid_moves(board: Board, color: Color) -> List[PlayerPosition]:

        valid_moves = []

        for position in board.get_all_positions():

            if GameRules.is_valid_move(board, position, color):

                valid_moves.append(position)

        return valid_moves

    @staticmethod
    def is_valid_move(board: Board, position: PlayerPosition, color: Color) -> bool:

        # To verify if the move is valid

        if board.get_cell(position) is not None:

            return False

        return len(GameRules.get_flipped_positions(board, position, color)) > 0


    @staticmethod
    def get_flipped_positions(board: Board, position: PlayerPosition, color: Color) -> List[PlayerPosition]:

        flipped = []

        for dr, dc in GameRules.Directions:
            flipped.extend(GameRules.__get_direction_flips(board, position, color, dr, dc))

        return flipped

    @staticmethod
    def __get_direction_flips(board: Board, position: PlayerPosition, color: Color, dr: int, dc: int) -> List[PlayerPosition]:

        """
        Returns all the positions in one direction
        """

        flipped = []

        r, c = position.row + dr, position.col + dc

        while 0 <= r < GameRules.Board_size and 0 <= c < GameRules.Board_size:

            current_posi = PlayerPosition(r, c)

            cell_pawn = board.get_cell(current_posi)

            if cell_pawn is None:

                return [] # No capture

            elif cell_pawn.color == color.opposite():

                flipped.append(current_posi)

            else: # cell_color == color

                if len(flipped) > 0:

                    return flipped

                else:

                    return []

            r, c = r + dr, c + dc

        return [] # exit the board

    @staticmethod
    def apply_move(board: Board, the_move: Move) -> Board:

        new_board = board.copy()

        new_board.set_cell(the_move.position, the_move.pawn)

        # Calculate and apply the flip

        flipped_positions = GameRules.get_flipped_positions(board, the_move.position, the_move.pawn)

        for pos in flipped_positions:

            new_board.set_cell(pos, the_move.pawn)

        the_move.flipped_position = flipped_positions

        return new_board

    @staticmethod
    def has_valid_moves(board: Board, pawn: Pawn) -> bool:
        """Vérifie si un joueur a des coups valides"""
        return len(GameRules.get_valid_moves(board, pawn)) > 0

    @staticmethod
    def get_winner(board: Board) -> Optional[Pawn]:

        # Determine the winner

        black_score = board.count_pawns(Color.BLACK)

        white_score = board.count_pawns(Color.WHITE)

        if black_score > white_score:

            return Color.BLACK

        elif white_score > black_score:

            return Color.WHITE

        return None



# 1️⃣ Create a board
#board = Board()

# 2️⃣ Place some pawns to simulate a real game state
#board.set_cell(PlayerPosition(3, 3), Pawn(Color.WHITE))
#board.set_cell(PlayerPosition(3, 4), Pawn(Color.BLACK))
#board.set_cell(PlayerPosition(4, 3), Pawn(Color.BLACK))
#board.set_cell(PlayerPosition(4, 4), Pawn(Color.WHITE))

# 3️⃣ Get all valid moves for BLACK
#valid_moves = GameRules.get_valid_moves(board, Color.BLACK)
#print("Valid moves for BLACK:", valid_moves)

# 4️⃣ Choose one of the valid moves and create a Move object
#if valid_moves:
    #chosen_position = valid_moves[0]
    #black_pawn = Pawn(Color.BLACK)
    #move = Move(chosen_position, black_pawn)

    # 5️⃣ Apply the move
    #new_board = GameRules.apply_move(board, move)

    #print("Flipped positions:", move.flipped_position)
