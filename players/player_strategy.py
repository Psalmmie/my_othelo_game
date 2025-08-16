from typing import Optional, Protocol
import random
from models.position import PlayerPosition as Position
from core.game_state import GameState
from core.game_rules import GameRules

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from console_ui import ConsoleUI

class PlayerStrategy(Protocol):
    """Interface pour les stratégies de joueur"""

    def choose_move(self, game_state: GameState) -> Optional[Position]:
        pass

    def get_name(self) -> str: ...


class HumanStrategy:
    """Stratégie pour joueur humain"""

    def __init__(self, ui: "ConsoleUI"):
        self.ui = ui

    def choose_move(self, game_state: GameState) -> Optional[Position]:
        valid_moves = GameRules.get_valid_moves(
            game_state.board, game_state.current_player
        )
        if not valid_moves:
            return None
        return self.ui.get_move_from_user(valid_moves)

    def get_name(self) -> str:
        return "Humain"


class RandomAIStrategy:
    """IA qui joue aléatoirement"""

    def choose_move(self, game_state: GameState) -> Optional[Position]:
        valid_moves = GameRules.get_valid_moves(
            game_state.board, game_state.current_player
        )
        return random.choice(valid_moves) if valid_moves else None

    def get_name(self) -> str:
        return "IA Aléatoire"
