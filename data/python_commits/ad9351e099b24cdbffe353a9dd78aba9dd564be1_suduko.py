import pygame
import numpy as np
import random

# Define the board size
board_size = 9
# Define the global range of numbers to try for each empty cell
num_range = list(range(1, 10))
# Shuffle the list of numbers to try
random.shuffle(num_range)



# Define the function to print the board
def print_board(board):
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=" ")
        print()

# Define the function to check if a move is valid
def is_valid_move(board, row, col, num):
    # Check row
    for i in range(board_size):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(board_size):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    # Move is valid
    return True

# Define the function to solve the board
def solve_board(board):
    # Find the next empty cell
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                # Try each number from 1 to 9
                for num in num_range:
                    if is_valid_move(board, i, j, num):
                        # Make the move
                        board[i][j] = num

                        # Recursively solve the rest of the board
                        if solve_board(board):
                            return True

                        # Undo the move
                        board[i][j] = 0

                # No valid move found
                return False

    # Board is solved
    return True

# Define the function to generate a random Sudoku puzzle
def generate_puzzle():
    # Start with a solved board
    board = np.zeros((board_size, board_size), dtype=int)
    solve_board(board)

    # Remove some numbers to create the puzzle
    num_removed = 0
    while num_removed < 50:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if board[row][col] != 0:
            temp = board[row][col]
            board[row][col] = 0
            temp_board = np.copy(board)
            if solve_board(temp_board) and np.count_nonzero(temp_board) == board_size * board_size:
                num_removed += 1
            else:
                board[row][col] = temp

    # Return the puzzle
    return board

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 540
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku")

# Set up the font
font = pygame.font.SysFont(None, 40)

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
light_gray = (192, 192, 192)
red = (255, 0, 0)

# Set up the game variables
selected_row = -1
selected_col = -1
game_over = False
solving = False
new_game = False
board = generate_puzzle()
board_copy = board.copy()

# Set up the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()

            # Check if the mouse is on the board
            if pos[0] >= 20 and pos[0] < 500 and pos[1] >= 20 and pos[1] < 500:
                # Get the row and column of the clicked cell
                selected_row = (pos[1] - 20) // 50
                selected_col = (pos[0] - 20) // 50
            else:
                selected_row = -1
                selected_col = -1

            # Check if the mouse is on the solve button
            if pos[0] >= 20 and pos[0] < 140 and pos[1] >= 540 and pos[1] < 580:
                solve_board(board)
                solving = True

            # Check if the mouse is on the new game button
            if pos[0] >= 160 and pos[0] < 340 and pos[1] >= 540 and pos[1] < 580:
                random.shuffle(num_range)
                board = generate_puzzle()
                board_copy = board.copy()
                solving = False

            # Check if the mouse is on the quit button
            if pos[0] >= 380 and pos[0] < 500 and pos[1] >= 540 and pos[1] < 580:
                game_over = True

    # Clear the screen
    screen.fill(white)

    # Draw the board
    for i in range(board_size):
        for j in range(board_size):
            # Draw the cell
            cell_rect = pygame.Rect(j * 50 + 20, i * 50 + 20, 50, 50)
            pygame.draw.rect(screen, black, cell_rect, 1)

            # Draw the number
            if board[i][j] != 0:
                if solving and board[i][j] != board_copy[i][j]:  # Check if solving and not an original number
                    number_color = (0, 128, 0)  # Set solved numbers to green
                else:
                    number_color = black
                number_text = font.render(str(board[i][j]), True, number_color)
                number_rect = number_text.get_rect(center=cell_rect.center)
                screen.blit(number_text, number_rect)
            # Draw the selection
            if i == selected_row and j == selected_col:
                pygame.draw.rect(screen, red, cell_rect, 3)

    # Draw the solve button
    solve_button_rect = pygame.Rect(20, 540, 120, 40)
    pygame.draw.rect(screen, gray, solve_button_rect)
    solve_button_text = font.render("Solve", True, black)
    solve_button_text_rect = solve_button_text.get_rect(center=solve_button_rect.center)
    screen.blit(solve_button_text, solve_button_text_rect)

    # Draw the new game button
    new_game_button_rect = pygame.Rect(160, 540, 180, 40)  # Make the button wider
    pygame.draw.rect(screen, gray, new_game_button_rect)
    new_game_button_text = font.render("New Game", True, black)
    new_game_button_text_rect = new_game_button_text.get_rect(center=new_game_button_rect.center)
    screen.blit(new_game_button_text, new_game_button_text_rect)

    # Draw the quit button
    quit_button_rect = pygame.Rect(380, 540, 120, 40)
    pygame.draw.rect(screen, gray, quit_button_rect)
    quit_button_text = font.render("Quit", True, black)
    quit_button_text_rect = quit_button_text.get_rect(center=quit_button_rect.center)
    screen.blit(quit_button_text, quit_button_text_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()