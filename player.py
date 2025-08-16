from typing import Optional
from color import Color
#from player_strategy import PlayerStrategy
from position import PlayerPosition as Position
from game_state import GameState
from player_strategy import PlayerStrategy

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from player_strategy import PlayerStrategy

class Player:

    def __init__(self, name: str, color: Color, strategy: PlayerStrategy):
        self.name = name
        self.color = color
        self.strategy = strategy

    def make_move(self, game_state: GameState) -> Optional[Position]:
        return self.strategy.choose_move(game_state)

    def get_name(self) -> str:
        return f"{self.name}"

    def get_color(self) -> Color:
        return self.color
