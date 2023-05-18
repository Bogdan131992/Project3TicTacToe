class TicTacToeGame:
    def __init__(self):
        """
        Initializesa new instance of the TicTacToe class.
        The board is represented as 3x3 grid, initially filed with empty spaces.
        The current player is set to "X" at the game start.
        """
        self.board = [["" for _ in range(3)] for _ in range (3)]
        self.current_player = "X"



def displayWelcomeMessage ():
    """
    Displays a welcome message at the start of the game
    """
    print ("Welcome to the interactive Tic Tac Toe game")

def print_board (self):
    """
    Prints the current state of the game board
    """
    print ("   0   1   2")
    for row in range (3):
        print (f"{row} " + " | ".join (self.board [row]))
        if row < 2:
            print ("  ---+---+---")


def check_winner(self):
    """
    Check if there is a winner in the current game board.
    Returns the Wining player ("X" sau "O"), "Tie" for a tie, or None if there is no winner yet.
    """
    # Check rows
    for row in self.board:
        if row [0] == row [1] == row [2] != " ":
            reurn row [0]

    # Check colums
    for col in range (3):
        if self.board [0][col] == self.board [1][col] == self.board [2][col] != " ":
            return self.board [0][col]
    # Check diagonals
    if self.board [0][0] == self.board [1][1] == self.board [2][2] != " ":
        return self.board [0][2]

     # Check for a tie
        if all(self.board[row][col] != " " for row in range(3) for col in range(3)):
            return "Tie"

        # No winner yet
        return None




def main():
    displayWelcomeMessage()
    print_board("")

main()