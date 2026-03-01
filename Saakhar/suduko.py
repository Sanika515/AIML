# Sudoku Solver using CSP (Backtracking + MRV + Forward Checking)

import copy

def print_board(board):
    for row in board:
        print(row)

def find_empty_cells(board):
    empty = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty.append((i, j))
    return empty

def is_valid(board, row, col, num):
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 grid
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def get_domain(board, row, col):
    domain = []
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            domain.append(num)
    return domain

def select_unassigned_variable(board):
    # MRV heuristic
    empty_cells = find_empty_cells(board)
    min_domain = 10
    selected = None

    for (row, col) in empty_cells:
        domain = get_domain(board, row, col)
        if len(domain) < min_domain:
            min_domain = len(domain)
            selected = (row, col)

    return selected

def solve_sudoku(board):
    cell = select_unassigned_variable(board)

    if not cell:
        return True  # Solved

    row, col = cell
    domain = get_domain(board, row, col)

    for num in domain:
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack

    return False


# Example Sudoku
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print("Original Sudoku:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("No solution exists")


    

#     Perfect 👩‍💻 Pallavi 👍
# Now I’ll explain your **CSP Sudoku Solver (Backtracking + MRV + Forward Checking)** clearly and in exam-friendly language.

# ---

# # 🧩 What This Program Does

# It solves Sudoku using:

# * ✅ Backtracking
# * ✅ MRV (Minimum Remaining Values heuristic)
# * ✅ Forward Checking (via domain filtering)

# It is a proper **Constraint Satisfaction Problem (CSP)** approach.

# ---

# # 🧠 CSP Mapping

# | CSP Term    | In Sudoku                              |
# | ----------- | -------------------------------------- |
# | Variable    | Empty cell                             |
# | Domain      | {1–9}                                  |
# | Constraints | No repetition in row, column, 3×3 grid |
# | Search      | Backtracking                           |
# | Heuristic   | MRV                                    |

# ---

# # 🔍 Function-by-Function Explanation

# ---

# ## 1️⃣ `print_board(board)`

# ```python
# def print_board(board):
#     for row in board:
#         print(row)
# ```

# ✔ Prints Sudoku row by row.
# ✔ Used to show original and solved puzzle.

# ---

# ## 2️⃣ `find_empty_cells(board)`

# ```python
# def find_empty_cells(board):
#     empty = []
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 empty.append((i, j))
#     return empty
# ```

# ✔ Finds all empty cells (value = 0).
# ✔ Returns list of positions like:

# ```
# [(0,2), (0,3), (1,1), ...]
# ```

# This helps MRV choose the best cell.

# ---

# ## 3️⃣ `is_valid(board, row, col, num)`

# This checks if placing a number follows constraints.

# ### 🔹 Row Check

# ```python
# for j in range(9):
#     if board[row][j] == num:
#         return False
# ```

# Number must not already exist in same row.

# ---

# ### 🔹 Column Check

# ```python
# for i in range(9):
#     if board[i][col] == num:
#         return False
# ```

# Number must not exist in same column.

# ---

# ### 🔹 3×3 Grid Check

# ```python
# start_row = row - row % 3
# start_col = col - col % 3
# ```

# Finds starting index of 3×3 grid.

# Then checks entire box:

# ```python
# for i in range(3):
#     for j in range(3):
#         if board[start_row + i][start_col + j] == num:
#             return False
# ```

# ✔ If no conflict → return True.

# ---

# ## 4️⃣ `get_domain(board, row, col)`

# ```python
# def get_domain(board, row, col):
#     domain = []
#     for num in range(1, 10):
#         if is_valid(board, row, col, num):
#             domain.append(num)
#     return domain
# ```

# ✔ Returns all possible valid values for a cell.
# ✔ This is Forward Checking.

# Example:

# If only 2 and 7 are allowed →
# Domain = `[2, 7]`

# This reduces search space.

# ---

# ## 5️⃣ `select_unassigned_variable(board)`

# ```python
# empty_cells = find_empty_cells(board)
# ```

# Gets all empty cells.

# Then:

# ```python
# domain = get_domain(board, row, col)
# ```

# Computes domain size for each.

# Then:

# ```python
# if len(domain) < min_domain:
# ```

# Chooses cell with **smallest domain**.

# This is:

# # ⭐ MRV (Minimum Remaining Values)

# ✔ Choose most constrained variable first
# ✔ Reduces branching
# ✔ Makes solving faster

# ---

# ## 6️⃣ `solve_sudoku(board)` (Main Algorithm)

# ### Step 1: Select cell using MRV

# ```python
# cell = select_unassigned_variable(board)
# ```

# If no cell left:

# ```python
# if not cell:
#     return True
# ```

# ✔ Puzzle solved.

# ---

# ### Step 2: Get domain

# ```python
# domain = get_domain(board, row, col)
# ```

# Possible values only.

# ---

# ### Step 3: Try each value

# ```python
# for num in domain:
# ```

# Try valid numbers only.

# ---

# ### Step 4: Assign value

# ```python
# board[row][col] = num
# ```

# ---

# ### Step 5: Recursive Call

# ```python
# if solve_sudoku(board):
#     return True
# ```

# Try solving rest of board.

# ---

# ### Step 6: Backtracking

# If failed:

# ```python
# board[row][col] = 0
# ```

# Undo assignment.

# Try next value.

# ---

# # 🔄 How This is Advanced Compared to Simple Version

# | Simple Backtracking  | This Version          |
# | -------------------- | --------------------- |
# | Try first empty cell | Use MRV               |
# | Try 1–9 blindly      | Use domain filtering  |
# | More recursive calls | Fewer recursive calls |
# | Slower               | Faster                |

# ---

# # 🧠 Why It Is Called Forward Checking?

# Because before assigning a value:

# * We check which values are possible
# * We reduce domain size early
# * We avoid unnecessary recursion

# ---

# # 📊 Algorithm Flow

# 1. Find empty cell using MRV
# 2. Get domain (possible values)
# 3. Try each value
# 4. Recursively solve
# 5. If fails → backtrack
# 6. If no empty left → solved

# ---

# # 🎯 Time Complexity

# Worst case:
# [
# O(9^{81})
# ]

# But with:

# * MRV
# * Domain filtering

# It becomes much faster in practice.

# ---

# # 📝 Viva Explanation (Very Clear Version)

# “This program models Sudoku as a Constraint Satisfaction Problem. Each empty cell is treated as a variable with domain 1–9. Row, column and 3×3 constraints are enforced using is_valid(). MRV heuristic selects the most constrained cell first, and forward checking reduces domain size. Backtracking is used to explore possible assignments until the puzzle is solved.”

# ---

# If you want next, I can:

# * 🔹 Draw recursion tree
# * 🔹 Show step-by-step solving of first 3 moves
# * 🔹 Give short 10-mark answer
# * 🔹 Compare Backtracking vs MRV clearly

# Tell me what you need 👩‍💻✨
