class Move:
    def __init__(self, marker, position):
        """
        Initializes a Move object with the specified marker and position.

        Parameters:
        - marker (str): The marker of the player making the move (X or O).
        - position (int): The position on the board where the move is made.
        """
        self.marker = marker
        self.position = position
