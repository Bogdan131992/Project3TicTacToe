class TicTacToeGame:
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





def main():
    displayWelcomeMessage()

main()