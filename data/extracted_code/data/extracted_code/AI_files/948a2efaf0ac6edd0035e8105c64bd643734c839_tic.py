def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    move_count = 0  # To track the number of moves

    while move_count < 9 and not check_winner(board):  # Max 9 moves
        print_board(board)

        # Get valid user input
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if 0 <= row < 3 and 0 <= col < 3:  # Ensure valid range for row and column
                    if board[row][col] == " ":
                        break  # If the spot is empty, exit the loop
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input! Row and column must be between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter integer values for row and column.")

        # Make the move
        board[row][col] = player
        move_count += 1

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    print_board(board)

    # After the loop ends, check for the winner
    if check_winner(board):
        # The player who made the last move is the winner
        if player == "X":
            print("Player O wins!")
        else:
            print("Player X wins!")
    else:
        print("It's a draw!")

tic_tac_toe()
