import os
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.text import Text
from typing import List, Optional
from models.position import PlayerPosition as Position
from core.game_state import GameState
from players.player import Player

#from typing import TYPE_CHECKING
#if TYPE_CHECKING:
#    from player import Player

clear = lambda: os.system("clear")


class ConsoleUI:
    """Interface console"""

    def __init__(self):
        self.console = Console()
        self._col_position_map = {i: chr(65 + i) for i in range(8)}
        self._reverse_col_position_map = {v: k for k, v in self._col_position_map.items()}

    def display_board(self, game_state: GameState) -> None:
        clear()

        # Création de la ligne score / coups / timer
        line = Table.grid(expand=True)
        line.add_column(justify="left")
        line.add_column(justify="center")
        line.add_column(justify="right")

        # Score (gauche)
        score_text = Text()
        score_text.append("⬤  ", style="bold bright_black")
        score_text.append(f"{game_state.black_score}", style="bold yellow")
        score_text.append("   ")
        score_text.append("⬤  ", style="white")
        score_text.append(f"{game_state.white_score}", style="bold yellow")

        # Nombre de coups (centre)
        moves_text = Text(f"Turn : {game_state.turn_number}", style="bold yellow")

        # Timer (droite): Check if method exists and works
        try:
            if hasattr(game_state, 'timer') and hasattr(game_state.timer, 'get_formatted_time'):
                game_time = game_state.timer.get_formatted_time()
                timer_text = Text(f"⏱ {game_time}", style="bold yellow")
            else:
                timer_text = Text("⏱ --:--", style="bold yellow")
        except Exception as e:
            timer_text = Text(f"⏱ ERROR", style="bold red")
            self.console.print(f"Timer error: {e}")

        # Ajouter la ligne complète
        line.add_row(score_text, moves_text, timer_text)

        # Affichage dans un Panel
        self.console.print(
            Panel(
                line,
                title="Play Othello",
                title_align="left",
                border_style="bold yellow",
                padding=(1, 2),
            )
        )

        
        edge_style = "bold white on #550000"
        cell_style = "white on #2E7D32"
        table = Table(
            # title=f"Au tour de {game_state.current_player.__rich__()}",
            box=box.SQUARE,
            show_lines=True,
            show_footer=True,
            style=cell_style,
            header_style=edge_style,
            footer_style=edge_style,
        )
        
        for col in range(10):
            header = "" if col == 0 or col == 9 else self._col_position_map[col-1]
            style = edge_style if col == 0 or col == 9 else cell_style
            table.add_column(
                header=header,
                footer=header,
                justify="center",
                style=style,
                header_style=edge_style,
                footer_style=edge_style,
                width= 3,
            )

        for row in range(8):
            row_data = [f"{row}"]
            for col in range(8):
                pos = Position(row, col)
                cell = game_state.board.get_cell(pos)
                if cell is None:
                    row_data.append(".")
                else:
                    row_data.append(cell.__rich__())
            row_data.append(f"{row}")
            table.add_row(*row_data)
        
        self.console.print("\n")
        self.console.print(table)

    def __math_pos_to_ui_pos(self, pos: Position) -> str:
        col = self._col_position_map[pos.col]
        return f"{col}{pos.row}"

    def __ui_pos_to_math_pos(self, pos: str) -> Position:
        col = self._reverse_col_position_map[pos[0]]
        row = int(pos[1])
        return Position(row, col)

    def get_move_from_user(self, valid_moves: List[Position]) -> Position:
        #self.console.print(f"valid moves: {[self.__math_pos_to_ui_pos(pos) for pos in valid_moves]}")
        while True:
            try:
                pos = input("Cell (ex: A1): ").strip().upper()
                self.console.print(f"You have chosen the position {pos}")
                position = self.__ui_pos_to_math_pos(pos)
                if position in valid_moves:
                    return position
                else:
                    self.console.print("Invalid move, try again.")
            except ValueError:
                self.console.print("Please enter the valid number.")
            except KeyboardInterrupt:
                self.console.print("\nGame Interuptted!.")
                exit(0)

    def display_message(self, message: str) -> None:
        self.console.print(message)

    def display_game_result(
        self, winner: Optional[Player], black_score: int, white_score: int
    ) -> None:
        clear()
        self.console.print(f"\n{'='*50}")
        self.console.print("End of Game!")
        self.console.print(f"Score final: ⚫️ {black_score} - ⚪️ {white_score}")
        if winner:
            self.console.print(f"🎉 {winner.get_name()} Winner!")
        else:
            self.console.print("🤝 Draw!")
        self.console.print(f"{'='*50}")
