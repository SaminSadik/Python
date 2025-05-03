# -- Main Game Loop -- #
def TicTacToe():
    print("Welcome to Tic-Tac-Toe!")
    player, playing = 1, True

    while playing:
        print_board()
        if player == 1:
            while True:
                move = input("Enter your move (1-9): ")
                if move.isdigit() and 1 <= int(move) <= 9:
                    row, col = divmod(int(move)-1, 3)
                    if available_square(row, col):
                        mark_square(row, col, 1)
                        break
                    else:
                        print("Invalid move, square already taken.")
                else:
                    print("Invalid input. Enter a number between 1 and 9.")
        else:
            ai_move()

        if check_win(player):
            playing = False
            print_board()
            print("AI wins!" if player != 1 else "You win")
        elif board_full():
            playing = False
            print_board()
            print("It's a tie!")
        else:
            player = 2 if player == 1 else 1

    print("-" * 11)

# -- Functional Operations -- #
board = [[0] * 3 for _ in range(3)]

def print_board():
    symbols = {0: '   ', 1: ' O ', 2: ' X '}
    print()
    for row in range(3):
        print("|".join(symbols[board[row][col]] for col in range(3)))
        if row < 2:
            print("-" * 11)
    print()

def available_square(row, col):
    return board[row][col] == 0

def mark_square(row, col, player):
    board[row][col] = player

def board_full():
    return all(board[row][col] != 0 for row in range(3) for col in range(3))

def check_win(player):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == player 
         or board[0][i] == board[1][i] == board[2][i] == player):
            return True

    if (board[0][0] == board[1][1] == board[2][2] == player 
     or board[0][2] == board[1][1] == board[2][0] == player):
        return True
    
    return False


# -- Logical Operations -- #
def minimax(minimax_board, depth, is_maximizing):
    if check_win(2): return float('inf')
    if check_win(1): return -float('inf')
    if board_full(): return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -float('inf')
    move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    mark_square(move[0], move[1], 2)
    print("Ai is thinking...")

# -- Run The Game -- #
TicTacToe()