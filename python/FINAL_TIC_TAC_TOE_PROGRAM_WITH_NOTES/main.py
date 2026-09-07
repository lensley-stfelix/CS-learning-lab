# ---------------------------------------------
# TIC-TAC-TOE FINAL VERSION (UNIT 2 COMPLETION)
# ---------------------------------------------

# Create the game board as a 2D list
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

# ---------------------------------------------
# Function: printBoard()
# Purpose: Display the current board to the user
# ---------------------------------------------
def printBoard():
    print(board[0])
    print(board[1])
    print(board[2])
    print()  # blank line for readability


# ---------------------------------------------------------
# Function: getMove(player)
# Purpose: Ask the player for a valid row/column input
# Uses loops + validation (Unit 2 concepts)
# ---------------------------------------------------------
def getMove(player):
    validMove = False

    while not validMove:
        # Ask for column
        col = 0
        while col < 1 or col > 3:
            col = int(input(player + " player, select a column 1-3: "))
            if col < 1 or col > 3:
                print("The column must be between 1 and 3.")

        # Ask for row
        row = 0
        while row < 1 or row > 3:
            row = int(input(player + " player, select a row 1-3: "))
            if row < 1 or row > 3:
                print("The row must be between 1 and 3.")

        # Convert to 0-based index
        col -= 1
        row -= 1

        # Check if spot is free
        if board[row][col] == "-":
            validMove = True
            return row, col  # return the valid move
        else:
            print("Oops, that spot was already taken. Please select another spot.")


# ---------------------------------------------------------
# Function: checkWin(player)
# Purpose: Check if the current player has won the game
# Covers rows, columns, and diagonals
# ---------------------------------------------------------
def checkWin(player):
    # Check rows
    for r in range(3):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            return True

    # Check columns
    for c in range(3):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False  # no win found


# ---------------------------------------------------------
# Function: playGame()
# Purpose: Main game loop (controls turns + win checking)
# ---------------------------------------------------------
def playGame():
    playerTurn = "X"  # X always starts
    printBoard()

    # Loop for max 9 turns (full board)
    for counter in range(1, 10):

        # Get a valid move from the player
        row, col = getMove(playerTurn)

        # Place the move on the board
        board[row][col] = playerTurn

        # Print updated board
        printBoard()

        # Check if the player won
        if checkWin(playerTurn):
            print(playerTurn, "wins the game!")
            return  # end the game immediately

        # Switch players
        if playerTurn == "X":
            playerTurn = "O"
        else:
            playerTurn = "X"

    # If loop finishes with no winner → tie
    print("It's a tie!")


# ---------------------------------------------------------
# Start the game
# ---------------------------------------------------------
playGame()
