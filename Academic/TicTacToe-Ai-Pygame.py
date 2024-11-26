import pygame
pygame.init()

def main():
    
    set_game()
    player, playing = 1, True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and playing:
                clicked_row = int(event.pos[1] // SQUARE_SIZE)
                clicked_col = int(event.pos[0] // SQUARE_SIZE)

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(1) or board_full(): playing = False
                    player = 2

            if player == 2 and playing:
                best_move()
                if check_win(2) or board_full(): playing = False
                player = 1

            if not playing: game_over()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    set_game()
                    player, playing = 1, True
                    
            pygame.display.update()

# --- CONSTANTS / VARIABLES ---

COLOR_BG = (93, 109, 126)
COLOR_LINE = (86, 101, 115)
COLOR_X = (236, 112, 99)
COLOR_O = (69, 179, 157)

WIDTH, HEIGHT = 360, 360
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS
RADIUS_O = SQUARE_SIZE // 3
WIDTH_X, WIDTH_O = 20, 15
WIDTH_LINE = 5
INF = float('inf')

board = [[0] * COLS for _ in range(ROWS)] # creates the game board
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # creates the game window

# --- Game Mechanics ---

def set_game():
    pygame.display.set_caption("Tic Tac Toe") # sets the title of the game window
    screen.fill(COLOR_BG) # fills the game UI with a color
    draw_lines() # draws the square devider line in the game UI
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0 # resets the board

def available_square(row, col):
    return board[row][col] == 0

def mark_square(row, col, player):
    board[row][col] = player
    draw_figures(row, col, player)

def board_full(check_board=board):
    for row in range(ROWS):
        for col in range(COLS):
            if check_board[row][col] == 0:
                return False
    return True

def check_win(player, check_board=board):
    for col in range(COLS):
        if check_board[0][col] == check_board[1][col] == check_board[2][col] == player:
            return True
    for row in range(ROWS):
        if check_board[row][0] == check_board[row][1] == check_board[row][2] == player:
            return True
    if check_board[0][0] == check_board[1][1] == check_board[2][2] == player:
        return True
    if check_board[0][2] == check_board[1][1] == check_board[2][0] == player:
        return True
    return False

def game_over():
    text = ""
    if board_full(): text = "tic tac Tie !"
    elif check_win(2): text = "You Lost !"
    else: text = "You Won?"
    pygame.display.set_caption(text + " press R to restart ")
    draw_lines(COLOR_BG)

# --- AI Functions ---

def minimax(minimax_board, depth, is_maximizing):
    if check_win(2, minimax_board): return INF # best score if AI wins
    elif check_win(1, minimax_board): return -INF # worst score if Human wins
    elif board_full(minimax_board): return 0 # Nurtal score, will tie
    
    if is_maximizing:
        best_score = -INF
        for row in range(ROWS):
            for col in range(COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth+1, False)
                    best_score = max(best_score, score)
                    minimax_board[row][col] = 0
        return best_score
    else:
        best_score = INF
        for row in range(ROWS):
            for col in range(COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth+1, True)
                    best_score = min(best_score, score)
                    minimax_board[row][col] = 0
        return best_score

def best_move():
    best_score, move = -INF, (-1, -1)

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score: 
                    best_score = score
                    move = (row, col)

    if move != (-1, -1): mark_square(move[0], move[1], 2)
    return


# --- UI Functions ---

def draw_lines(color=COLOR_LINE):
    for i in range(1, ROWS):
        pygame.draw.line(
            screen, color, width=WIDTH_LINE,
            start_pos=(0, i*SQUARE_SIZE), end_pos=(WIDTH, i*SQUARE_SIZE)
        )
        pygame.draw.line(
            screen, color, width=WIDTH_LINE,
            start_pos=(i*SQUARE_SIZE, 0), end_pos=(i*SQUARE_SIZE, HEIGHT)
        )

def draw_figures(row, col, player):
    color1, color2 = COLOR_O, COLOR_X
    if player == 1:
        pygame.draw.circle(
            screen, color1, width=WIDTH_O, 
            radius=RADIUS_O, 
            center=(col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2)
        )
    else:
        pygame.draw.line(
            screen, color2, width=WIDTH_X, 
            start_pos=(col*SQUARE_SIZE + SQUARE_SIZE//4, row*SQUARE_SIZE + SQUARE_SIZE//4), 
            end_pos=(col*SQUARE_SIZE + 3*SQUARE_SIZE//4, row*SQUARE_SIZE + 3*SQUARE_SIZE//4)
        )
        pygame.draw.line(
            screen, color2, width=WIDTH_X,
            start_pos=(col*SQUARE_SIZE + SQUARE_SIZE//4, row*SQUARE_SIZE + 3*SQUARE_SIZE//4), 
            end_pos=(col*SQUARE_SIZE + 3*SQUARE_SIZE//4, row*SQUARE_SIZE + SQUARE_SIZE//4)
        )


main() # run the game