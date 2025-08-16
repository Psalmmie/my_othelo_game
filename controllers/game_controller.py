from models.color import Color
from ui.console_ui import ConsoleUI
from players.player_strategy import PlayerStrategy
from players.player import Player
from core.engine import Engine as Game

class GameController:

    """Contrôleur principal - Responsabilité : orchestration"""
    
    def __init__(self, ui: ConsoleUI, player1_strategy: PlayerStrategy, player2_strategy: PlayerStrategy):
        
        self.__ui = ui
        
        player1 = Player("Player 1", Color.BLACK, strategy=player1_strategy)
        
        player2 = Player("Player 2", Color.WHITE, strategy=player2_strategy)
        
        self.__game = Game(player1, player2)

    def run_game_loop(self) -> None:
        
        """Boucle principale du jeu"""
        
        self.__ui.display_message("=== DÉBUT DE LA PARTIE D'OTHELLO ===")

        self.__game.start_game()

        consecutive_passes = 0

        # ToDO: consecutive_passes est necessaire ?
        while not self.__game.is_finished() and consecutive_passes < 2:
           
            state = self.__game.get_state()
            
            self.__ui.display_board(state)

            current_player = self.__game.get_current_player()
            
            self.__ui.display_message(f"\nTurn {current_player.get_name()}")

            result = self.__game.play_turn()

            if result.success:
                
                consecutive_passes = 0
                
                self.__ui.display_message(result.message)
            
            else:
                
                consecutive_passes += 1
                
                self.__ui.display_message(f"❌ {result.message} - Passing the turn")

        # Afficher le résultat final
        final_state = self.__game.get_state()
        
        winner = self.__game.get_winner()

        final_time = self.__game.get_final_time()
        
        self.__ui.display_game_result(winner, final_state.black_score, final_state.white_score)
