from typing import Optional
from game_state import GameState
from player_move import Move

class MoveResult:

    """
    The result of a move
    """

    def __init__(self, success: bool, message: str, move: Optional[Move] = None, new_state: Optional[GameState] = None):

        self.success = success # the attributes

        self.message = message # attributes

        self.move = move

        self.new_state = new_state
