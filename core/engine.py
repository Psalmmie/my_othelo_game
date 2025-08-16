from core.board import Board 
from models.position import PlayerPosition as Position
from models.color import Color 
from players.player import Player 
from models.pawn import Pawn 
from core.game_rules import GameRules
from core.game_status import GameStatus
from models.player_move import Move
from typing import Optional 
from core.game_state import GameState   
from models.move_result import MoveResult

class Engine:
    """Orchestrateur principal du jeu - Responsabilité unique : gestion de l'état"""
    def __init__(self, player1: Player, player2: Player):
        # Initialisation du plateau
        board = Board()
        board.set_cell(Position(3, 3), Pawn(Color.BLACK))
        board.set_cell(Position(3, 4), Pawn(Color.WHITE))
        board.set_cell(Position(4, 3), Pawn(Color.WHITE))
        board.set_cell(Position(4, 4), Pawn(Color.BLACK))
        
        self.__state = GameState(board, Color.BLACK)
        self.__players = [player1, player2]
        # self.__history = MoveHistory()
        self.__current_player_index = 0
    
    def start_game(self) -> None:
        """ Start the game and timer """
        self.__state.start_timer()

    def get_state(self) -> GameState:
        return self.__state.copy()
    
    def get_current_player(self) -> Player:
        return self.__players[self.__current_player_index]
    
    def play_turn(self) -> MoveResult:
        """Joue un tour et retourne le résultat"""
        current_player = self.get_current_player()
        
        # Vérifier si le joueur peut jouer
        if not GameRules.has_valid_moves(self.__state.board, current_player.color):
            return MoveResult(False, f"{current_player.name} cannot play")
        
        # Demander le coup au joueur
        position = current_player.make_move(self.__state)
        if not position:
            return MoveResult(False, "No move chosen")
        
        # Vérifier la validité
        if not GameRules.is_valid_move(self.__state.board, position, current_player.color):
            return MoveResult(False, "Invalid move")
        
        pawn = Pawn(current_player.color)
        move = Move(position, pawn)
        new_board = GameRules.apply_move(self.__state.board, move)
        # Appliquer le coup
        #move = Move(position, current_player.color)
        #new_board = GameRules.apply_move(self.__state.board, move)
        
        # Sauvegarder l'ancien état
        # self.__history.add_move(move, self.__state)
        
        # Mettre à jour l'état
        old_timer = self.__state.timer
        self.__state = GameState(new_board, current_player.color.opposite())
        self.__state.timer = old_timer
        self.__state.turn_number += 1
        # self.__state.turn_number = self.__history.get_move_count()
        
        # Vérifier fin de partie
        if self.__check_game_over():
            self.__state.status = GameStatus.FINISHED
            final_time = self.__state.stop_timer()
        
        self.__switch_player()
        return MoveResult(True, f"Move played in {position}", move, self.__state.copy())
    
    def __check_game_over(self) -> bool:
        """Vérifie si la partie est terminée"""
        if self.__state.board.is_full():
            return True
        
        # Vérifier si aucun joueur ne peut jouer
        for player in self.__players:
            if GameRules.has_valid_moves(self.__state.board, player.color):
                return False
        
        return True
    
    def __switch_player(self) -> None:
        self.__current_player_index = 1 - self.__current_player_index
    
    def is_finished(self) -> bool:
        return self.__state.status == GameStatus.FINISHED
    
    def get_winner(self) -> Optional[Player]:
        if not self.is_finished():
            return None
        
        winner_color = GameRules.get_winner(self.__state.board)
        if winner_color is None:
            return None
        
        winner = None
        for player in self.__players:
            if player.color == winner_color:
                winner = player
                break
        return winner

    def get_final_time(self) -> str:

        """Get the final game time"""

        return self.__state.timer.get_detailed_time()
