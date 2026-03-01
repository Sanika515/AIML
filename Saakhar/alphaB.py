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


def alphabeta(board, alpha, beta, is_max):
    winner = check_winner(board)

    if winner == 'X':
        return 1
    if winner == 'O':
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        value = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                value = max(value, alphabeta(board, alpha, beta, False))
                board[i] = ' '
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
        return value
    else:
        value = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                value = min(value, alphabeta(board, alpha, beta, True))
                board[i] = ' '
                beta = min(beta, value)
                if beta <= alpha:
                    break
        return value


def best_move(board):
    best_val = -100
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = alphabeta(board, -100, 100, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move


# Game Start
board = [' '] * 9

while True:
    print_board(board)

    # User Move
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

    # Computer Move
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






# # ✅ 1️⃣ `print_board(board)`

# ```python
# def print_board(board):
# ```

# This function prints the board in 3×3 format.

# ```python
# for i in range(0, 9, 3):
#     print(board[i], "|", board[i+1], "|", board[i+2])
# ```

# It prints 3 elements per row.

# Example:

# ```
# X | O |  
#   | X |  
#   |   | O
# ```

# ---

# # ✅ 2️⃣ `check_winner(board)`

# This function checks if someone won.

# ```python
# wins = [(0,1,2),(3,4,5),(6,7,8),
#         (0,3,6),(1,4,7),(2,5,8),
#         (0,4,8),(2,4,6)]
# ```

# These are all possible winning combinations:

# * 3 rows
# * 3 columns
# * 2 diagonals

# If 3 positions match → return `'X'` or `'O'`.

# If no winner → return `None`.

# ---

# # ✅ 3️⃣ `alphabeta(board, alpha, beta, is_max)`

# This is the main AI function.

# ### Parameters:

# * `board` → current board
# * `alpha` → best value for maximizing player (X)
# * `beta` → best value for minimizing player (O)
# * `is_max` → True if it's X’s turn

# ---

# ## 🔹 Step A: Base Case (Game Over)

# ```python
# winner = check_winner(board)
# ```

# If:

# * X wins → return `1`
# * O wins → return `-1`
# * Draw → return `0`

# This stops recursion.

# ---

# ## 🔹 Step B: Maximizing Player (Computer - X)

# ```python
# if is_max:
# ```

# Computer wants highest score.

# ```python
# value = -100
# ```

# Try every empty position:

# ```python
# board[i] = 'X'
# ```

# Call recursively:

# ```python
# value = max(value, alphabeta(...))
# ```

# Undo move:

# ```python
# board[i] = ' '
# ```

# Update alpha:

# ```python
# alpha = max(alpha, value)
# ```

# ---

# ### 🔥 Pruning Condition

# ```python
# if alpha >= beta:
#     break
# ```

# If alpha ≥ beta:

# * No need to check further
# * Stop exploring this branch
# * Saves time

# ---

# ## 🔹 Step C: Minimizing Player (User - O)

# ```python
# else:
# ```

# User wants lowest score.

# ```python
# value = 100
# ```

# Try all empty positions.

# Update beta:

# ```python
# beta = min(beta, value)
# ```

# If:

# ```python
# beta <= alpha:
# ```

# Stop checking (prune branch).

# ---

# # ✅ 4️⃣ `best_move(board)`

# This function decides computer move.

# ```python
# for i in range(9):
# ```

# Try all empty positions.

# Temporarily place `'X'`.

# Call:

# ```python
# move_val = alphabeta(board, -100, 100, False)
# ```

# Choose move with highest value.

# Return best move index.

# ---

# # ✅ 5️⃣ Main Game Loop

# ```python
# while True:
# ```

# Game continues until:

# * User wins
# * Computer wins
# * Draw

# ---

# ## 🔹 User Move

# ```python
# user_move = int(input("Enter position (0-8): "))
# ```

# User enters number 0–8.

# Board updated with `'O'`.

# ---

# ## 🔹 Computer Move

# ```python
# comp_move = best_move(board)
# ```

# Computer calculates best move using Alpha-Beta.

# Places `'X'`.

# ---

# # ✅ Why Alpha–Beta Is Better Than Normal Minimax?

# Minimax:

# * Checks all branches.

# Alpha–Beta:

# * Skips useless branches.
# * Faster.
# * Same result.

# ---

# # ✅ Simple Summary

# 1. User enters move
# 2. Computer calculates optimal move
# 3. Alpha–Beta reduces unnecessary calculations
# 4. Game continues until win or draw

# ---

# # ✅ Viva Answer (Short)

# > Alpha–Beta pruning is an optimized version of Minimax.
# > Alpha stores best value for maximizing player.
# > Beta stores best value for minimizing player.
# > If alpha ≥ beta, branch is pruned.
# > It gives same result but faster.

# ---

# If you want, I can:

# * Draw tree diagram
# * Show step-by-step sample move
# * Compare Minimax vs Alpha-Beta clearly

# Tell me 😊
