class FileHandler:
    def __init__(self, file_path):
        """
        Initializes the FileHandler object with the specified file path.

        Parameters:
        - file_path (str): The path to the file for recording moves.
        """
        self.file_path = file_path

    def record_move(self, marker, position):
        """
        Records a player's move in the file.

        Parameters:
        - marker (str): The marker (X or O) of the player making the move.
        - position (int): The position on the board where the move is made.
        """
        with open(self.file_path, "a") as file:
            file.write(f"{marker}:{position} ")

    def reset_game_file(self):
        """
        Resets the game file by truncating its content.
        """
        with open(self.file_path, "w") as file:
            file.truncate(0)
