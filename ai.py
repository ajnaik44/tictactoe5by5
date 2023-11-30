from player import Player

class AI(Player):
    def __init__(self, marker):
        """
        Initializes the AI player with the specified marker and determines the opponent's marker.

        Parameters:
        - marker (str): The marker of the AI player (X or O).
        """
        super().__init__(marker)
        self.opponent_marker = "O" if marker == "X" else "X"

    def find_best_move(self, board):
        """
        Finds the best move for the AI using the minimax algorithm.

        Parameters:
        - board (Board): The game board.

        Returns:
        - int: The best move for the AI.
        """
        best_score, best_move = self.minimax(board, 0, False, float('-inf'), float('inf'))
        return best_move

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Implements the minimax algorithm to determine the best move.

        Parameters:
        - board (Board): The game board.
        - depth (int): The current depth in the search tree.
        - is_maximizing (bool): True if the AI is maximizing, False if minimizing.
        - alpha (float): The alpha value for alpha-beta pruning.
        - beta (float): The beta value for alpha-beta pruning.

        Returns:
        - tuple: A tuple containing the best score and the corresponding best move.
        """
        if board.is_winner(self.marker):
            return 1, None
        elif board.is_winner(self.opponent_marker):
            return -1, None
        elif board.is_tie():
            return 0, None

        if depth >= 4:  # Limit the depth to prevent infinite loop
            return 0, None

        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = None

        for move in board.available_moves():
            board.cells[move] = self.marker if is_maximizing else self.opponent_marker
            score, _ = self.minimax(board, depth + 1, not is_maximizing, alpha, beta)
            board.cells[move] = " "

            if is_maximizing:
                if score > best_score:
                    best_score = score
                    best_move = move
                    alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            else:
                if score < best_score:
                    best_score = score
                    best_move = move
                    beta = min(beta, best_score)
                if beta <= alpha:
                    break

        return best_score, best_move
