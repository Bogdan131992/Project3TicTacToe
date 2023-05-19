class TicTacToeGame:
    def __init__(self):
        """
        Initializes a new instance of the TicTacToe class.
        The board is represented as a 3x3 grid,
        initially filled with empty spaces.
        The current player is set to "X" to start the game.
        """
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        """
        Prints the current state of the game board.
        """
        print("   0   1   2")
        for row in range(3):
            print(f"{row}  " + " | ".join(self.board[row]))
            if row < 2:
                print("  ---+---+---")

    def check_winner(self):
        """
        Checks if there is a winner in the current game board.
        Returns: str or None: The winning player ("X" or "O"),
        "Tie" for a tie, or None if there is no winner yet.
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Check columns
        board = self.board
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        # Check for a tie
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    break
            else:
                continue
            break
        else:
            return "Tie"

        # No winner yet
        return None


def main():
    """
    Plays a game of Tic-Tac-Toe.
    This function allows two players to take turns
    entering their moves and updates the game board accordingly.
    The players are represented by "X" and "O".
    The game continues until there is a winner or a tie.
    """
    print("Welcome to the interactive Tic Tac Toe game")
    print("Your move should contain two numbers (row [space] column)")
    game = TicTacToeGame()

    while True:
        game.print_board()
        try:
            move = input(f"Player {game.current_player}, enter your move: ")
            row, col = map(int, move.split())

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid move. Enter numbers between 0 and 2.")
                continue

            if game.board[row][col] != " ":
                print("Invalid move. That position is already occupied.")
                continue

            game.board[row][col] = game.current_player

            winner = game.check_winner()
            if winner:
                game.print_board()
                if winner == "Tie":
                    print("It's a tie!")
                else:
                    print(f"Player {winner} wins!")
                break

            game.current_player = "O" if game.current_player == "X" else "X"

        except ValueError:
            print("Invalid input.Enter two integers separated by a space.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            break


if __name__ == '__main__':
    main()
