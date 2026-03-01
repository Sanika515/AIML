def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()


def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None


def minimax(board, is_max):
    winner = check_winner(board)

    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, False))
                board[i] = ' '
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, True))
                board[i] = ' '
        return best


def best_move(board):
    best_val = -100
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move


# Game Start
board = [' '] * 9

while True:
    print_board(board)

    # User move
    user_move = int(input("Enter position (0-8): "))
    if board[user_move] != ' ':
        print("Invalid move! Try again.")
        continue

    board[user_move] = 'O'

    if check_winner(board):
        print_board(board)
        print("You Win!")
        break

    if ' ' not in board:
        print_board(board)
        print("Draw!")
        break

    # Computer move
    comp_move = best_move(board)
    board[comp_move] = 'X'

    if check_winner(board):
        print_board(board)
        print("Computer Wins!")
        break

    if ' ' not in board:
        print_board(board)
        print("Draw!")
        break



# 🔹 What is Minimax?

# Minimax is a decision-making algorithm used in two-player games.

# X → Maximizing player

# O → Minimizing player

# X tries to maximize score
# O tries to minimize score

# 🔹 How It Works
# 1️⃣ Check Winner

# If:

# X wins → return +1

# O wins → return -1

# Draw → return 0

# 2️⃣ Maximizing Step (X)

# Try every empty space.

# Recursively call minimax.

# Choose move with maximum value.

# 3️⃣ Minimizing Step (O)

# Try every empty space.

# Recursively call minimax.

# Choose move with minimum value.

# 4️⃣ Best Move Function

# Tests all possible moves.

# Calls minimax.

# Returns best move index.

# ✅ Why Minimax Works

# It explores all possible future game states.
# Assumes opponent plays optimally.
# Guarantees best possible move.

# ✅ Time Complexity
# O(b^d)