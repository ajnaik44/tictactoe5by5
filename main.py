from file_handler import FileHandler
from board import Board
from player import Player
from ai import AI
from game import Game

def main():
    """
    The main function that initializes and starts the Tic Tac Toe game.
    """
    file_handler = FileHandler("tictactoe.txt")
    board = Board(file_handler)
    player = Player("X")
    ai = AI("O")
    game = Game(board, ai, player, file_handler)
    game.start_game()

if __name__ == "__main__":
    main()
