import os

class Board:
    def __init__(self, file_handler):
        """
        Initializes the Board object with an empty 5x5 board and a file handler.

        Parameters:
        - file_handler (FileHandler): The file handler for recording moves.
        """
        self.cells = [" "] * 26  # 5x5 board
        self.file_handler = file_handler

    def _clear_screen(self):
        """
        Clears the console screen.
        """
        os.system("clear")

    def is_tie(self):
        """
        Checks if the game is a tie.

        Returns:
        - bool: True if the game is a tie, False otherwise.
        """
        return " " not in self.cells[1:]

    def is_winner(self, player):
        """
        Checks if the specified player has won the game.

        Parameters:
        - player (str): The player marker (X or O).

        Returns:
        - bool: True if the player has won, False otherwise.
        """
        # Check rows
        for i in range(1, 22, 5):
            if self.cells[i:i+5] == [player] * 5:
                return True

        # Check columns
        for i in range(1, 6):
            column = [self.cells[i + j * 5] for j in range(5)]
            if column == [player] * 5:
                return True

        # Check diagonals
        if self.cells[1] == self.cells[7] == self.cells[13] == self.cells[19] == player or self.cells[5] == self.cells[9] == self.cells[13] == self.cells[17] == player:
            return True

        return False

    def is_space_available(self, position):
        """
        Checks if the specified board position is available.

        Parameters:
        - position (int): The position on the board to check.

        Returns:
        - bool: True if the position is available, False otherwise.
        """
        return self.cells[position] == " "

    def update_board(self, move):
        """
        Updates the board with the specified move and checks for a winner or a tie.

        Parameters:
        - move (Move): The move to be applied.

        Returns:
        - str or None: A message indicating the result (winner or tie), or None if the game continues.
        """
        if self.is_space_available(move.position):
            self.cells[move.position] = move.marker
            self.file_handler.record_move(move.marker, move.position)
            if self.is_winner(move.marker):
                return f"\n{move.marker} wins!"
            if self.is_tie():
                return "\nIt's a draw!"
        else:
            return "Cell is already taken"

    def display(self):
        """
        Displays the current state of the board on the console.
        """
        self._clear_screen()
        for i in range(1, 26, 5):
            print(" | ".join(self.cells[i:i+5]))
            if i < 21:
                print("-" * 17)

    def available_moves(self):
        """
        Returns a list of available moves on the board.

        Returns:
        - list: A list of available moves (positions).
        """
        available_moves_list = []
        for i in range(1, 26):
            if self.cells[i] == " ":
                available_moves_list.append(i)
        return available_moves_list
