# Tic Tac Toe Game

# Create the board
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print(board[0])
print(board[1])
print(board[2])

# Player X always starts
playerTurn = "X"

# Loop for all 9 turns
for counter in range(1, 10):

    col = 0
    row = 0

    # --- COLUMN VALIDATION (Item #1) ---
    while col < 1 or col > 3:
        col = int(input(playerTurn + " player, select a column 1-3: "))
        if col < 1 or col > 3:
            print("The column must be between 1 and 3.")

    # --- ROW VALIDATION (Item #1) ---
    while row < 1 or row > 3:
        row = int(input(playerTurn + " player, select a row 1-3: "))
        if row < 1 or row > 3:
            print("The row must be between 1 and 3.")

    # Convert to 0-based indexing
    col -= 1
    row -= 1

    # --- SPOT VALIDATION (Item #2) ---
    while True:
        if board[row][col] == "-":
            board[row][col] = playerTurn
            break
        else:
            print("Oops, that spot was already taken.")
            # Ask again
            col = 0
            row = 0

            while col < 1 or col > 3:
                col = int(input(playerTurn + " player, select a column 1-3: "))
                if col < 1 or col > 3:
                    print("The column must be between 1 and 3.")

            while row < 1 or row > 3:
                row = int(input(playerTurn + " player, select a row 1-3: "))
                if row < 1 or row > 3:
                    print("The row must be between 1 and 3.")

            col -= 1
            row -= 1

    # Print updated board
    print(board[0])
    print(board[1])
    print(board[2])

    # Switch player
    if playerTurn == "X":
        playerTurn = "O"
    else:
        playerTurn = "X"
