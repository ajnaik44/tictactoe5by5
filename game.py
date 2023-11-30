import random

class Game:
    def __init__(self, board, ai, player, file_handler):
        """
        Initializes the Game object with the given board, AI, player, and file handler.

        Parameters:
        - board (Board): The game board.
        - ai (AI): The AI player.
        - player (Player): The human player.
        - file_handler (FileHandler): The file handler for game data.
        """
        self.board = board
        self.ai = ai
        self.player = player
        self.file_handler = file_handler
        self.starting_player = random.choice([player, ai])

    def display_ui(self):
        """
        Displays the game UI, including the current state of the board and player markers.
        """
        self.board.display()
        print("\nPlayer:", self.player.marker)
        print("AI:", self.ai.marker)

    def get_user_choice(self):
        """
        Gets the user's choice for a move, ensuring it is a valid and available cell.

        Returns:
        - int: The user's chosen cell number.
        """
        while True:
            try:
                user_choice = int(input("\nChoose a cell (1 - 25): "))
                if 1 <= user_choice <= 25:
                    if self.board.is_space_available(user_choice):
                        return user_choice
                    else:
                        self.display_ui()
                        print("\nCell is already taken. Please choose an available cell.")
                else:
                    self.display_ui()
                    print("\nPlease enter a number between 1 and 25.")
            except ValueError:
                self.display_ui()
                print("\nPlease enter a valid number.")

    def start_game(self):
        """
        Starts the game loop, allowing players to take turns until a winner is determined.
        """
        self.file_handler.reset_game_file()

        while True:
            self.display_ui()
            move = None

            if self.starting_player == self.player:
                player_choice = self.get_user_choice()
                move = self.player.make_move(player_choice)
            else:
                print("\nAI's choosing...")
                ai_choice = self.ai.find_best_move(self.board)
                move = self.ai.make_move(ai_choice)
            
            result = self.board.update_board(move)

            if result is not None:
                self.display_ui()
                print(result)
                break
                
            # Switch the starting player for the next turn
            self.starting_player = self.player if self.starting_player == self.ai else self.ai
