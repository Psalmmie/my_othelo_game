from core.game_status import GameStatus
from models.color import Color
from models.pawn import Pawn
from core.board import Board
from core.game_timer import GameTimer

class GameState:

    """Complete game status data class"""
    
    def __init__(self, board: Board, current_player: Color):
        
        self.board = board

        self.current_player = current_player
        
        self.status = GameStatus.IN_PROGRESS
        
        self.black_score = board.count_pawns(Color.BLACK)
        
        self.white_score = board.count_pawns(Color.WHITE)
        
        self.turn_number = 0
        
        self.timer = GameTimer()
    
    def copy(self) -> 'GameState':
        
        new_state = GameState(self.board.copy(), self.current_player)
        
        new_state.status = self.status
        
        new_state.black_score = self.black_score
        
        new_state.white_score = self.white_score
        
        new_state.turn_number = self.turn_number

        new_state.timer = self.timer
        
        return new_state
    
    def is_terminal(self) -> bool:
        
        return self.status == GameStatus.FINISHED


    def start_timer(self) -> None:
        
        """Start the game timer"""
        
        self.timer.start()

    def pause_timer(self) -> None:
        
        """Pause the game timer"""
        
        self.timer.pause()

    def resume_timer(self) -> None:
        
        """Resume the game timer"""
        
        self.timer.resume()

    def stop_timer(self) -> float:
        
        """Stop the timer and return elapsed time"""
        
        return self.timer.stop()

    def get_game_time(self) -> str:
        
        """Get formatted game time"""
        
        return self.timer.get_formatted_time()

#Create initial game state
#initial_board = Board()
# Set up initial Othello position
#initial_board.set_cell(PlayerPosition(3, 3), Pawn(Color.WHITE))
#initial_board.set_cell(PlayerPosition(3, 4), Pawn(Color.BLACK)) 
#initial_board.set_cell(PlayerPosition(4, 3), Pawn(Color.BLACK))
#initial_board.set_cell(PlayerPosition(4, 4), Pawn(Color.WHITE))

# Create game state with BLACK starting (standard Othello)
#game_state = GameState(initial_board, Color.BLACK)

#print(game_state)  # Shows current state
#print(f"Black score: {game_state.black_score}")
#print(f"White score: {game_state.white_score}")

