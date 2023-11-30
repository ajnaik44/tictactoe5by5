from move import Move

class Player:
    def __init__(self, marker):
        """
        Initializes a Player object with the specified marker.

        Parameters:
        - marker (str): The marker of the player (X or O).
        """
        self.marker = marker

    def make_move(self, position):
        """
        Creates a Move object representing the player's move.

        Parameters:
        - position (int): The position on the board where the move is made.

        Returns:
        - Move: A Move object representing the player's move.
        """
        return Move(self.marker, position)
