from console_ui import ConsoleUI
from player_strategy import HumanStrategy
from game_controller import GameController


def main():
    """Fonction principale pour tester le jeu"""
    ui = ConsoleUI()
    human1 = HumanStrategy(ui)
    human2 = HumanStrategy(ui)
    game_controller = GameController(ui, human1, human2)
    game_controller.run_game_loop()

if __name__ == "__main__":
    main()
