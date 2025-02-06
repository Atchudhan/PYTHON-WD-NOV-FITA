import pygame, sys
import numpy as np

# initializes pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
LINE_WIDTH = 10
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 20
SPACE = 55

# Colors
BG_COLOR = (40, 40, 40)  # Dark background
LINE_COLOR = (200, 200, 200)
CIRCLE_COLOR = (220, 220, 220)
CROSS_COLOR = (255, 100, 100)
GLOW_COLOR = (255, 255, 0)
HOVER_COLOR = (100, 100, 100)
TEXT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe 3D")
screen.fill(BG_COLOR)

# Board setup
board = np.zeros((BOARD_ROWS, BOARD_COLS))
font = pygame.font.Font(None, 50)

# Get player names
player1_name = input("Enter Player 1 name (X): ") or "Player X"
player2_name = input("Enter Player 2 name (O): ") or "Player O"
player_names = {1: player1_name, 2: player2_name}

winner = None

def draw_board():
    screen.fill(BG_COLOR)
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                start_pos1 = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_pos1 = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_pos1, end_pos1, CROSS_WIDTH)
                
                start_pos2 = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_pos2 = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_pos2, end_pos2, CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def check_win(player):
    global winner
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_winning_line(col, 'vertical', player)
            winner = player
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_winning_line(row, 'horizontal', player)
            winner = player
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_winning_line(0, 'desc', player)
        winner = player
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        draw_winning_line(0, 'asc', player)
        winner = player
        return True
    return False

def draw_winning_line(index, direction, player):
    glow_color = GLOW_COLOR if player == 1 else (255, 50, 50)
    if direction == 'vertical':
        pygame.draw.line(screen, glow_color, (index * SQUARE_SIZE + SQUARE_SIZE // 2, 15), (index * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 15), 15)
    elif direction == 'horizontal':
        pygame.draw.line(screen, glow_color, (15, index * SQUARE_SIZE + SQUARE_SIZE // 2), (WIDTH - 15, index * SQUARE_SIZE + SQUARE_SIZE // 2), 15)
    elif direction == 'desc':
        pygame.draw.line(screen, glow_color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)
    elif direction == 'asc':
        pygame.draw.line(screen, glow_color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def hover_effect():
    mouseX, mouseY = pygame.mouse.get_pos()
    hovered_row, hovered_col = mouseY // SQUARE_SIZE, mouseX // SQUARE_SIZE
    if available_square(hovered_row, hovered_col):
        pygame.draw.rect(screen, HOVER_COLOR, (hovered_col * SQUARE_SIZE, hovered_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def display_winner():
    if winner:
        text = font.render(f"Winner: {player_names[winner]}", True, TEXT_COLOR)
        screen.blit(text, (WIDTH // 4, HEIGHT // 2))

def restart():
    global board, game_over, player, winner
    board = np.zeros((BOARD_ROWS, BOARD_COLS))
    game_over = False
    player = 1
    winner = None
    draw_board()

draw_board()
player = 1
game_over = False

while True:
    screen.fill(BG_COLOR)
    draw_board()
    draw_figures()
    hover_effect()
    display_winner()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row, clicked_col = mouseY // SQUARE_SIZE, mouseX // SQUARE_SIZE
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
    pygame.display.update()
