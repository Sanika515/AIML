# N-Queen Problem using CSP (Backtracking)

def is_safe(board, row, col, n):
    
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check diagonal (upper left & upper right)
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    
    return True


def solve_nqueen(board, row, n):
    
    if row == n:
        return True   # All queens placed successfully
    
    for col in range(n):
        if is_safe(board, row, col, n):
            
            board[row] = col   # Place queen
            
            if solve_nqueen(board, row + 1, n):
                return True
            
            board[row] = -1   # Backtrack
    
    return False


def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# -------- Main --------
n = int(input("Enter value of N: "))

board = [-1] * n   # board[i] = column of queen in row i

if solve_nqueen(board, 0, n):
    print("\nSolution Found:\n")
    print_solution(board, n)
else:
    print("No solution exists")


#     1️⃣ Board Representation
# board = [-1] * n

# Instead of 2D board, we use 1D array:

# board[i] = j

# Means queen is placed at row i, column j

# Example:

# board = [1, 3, 0, 2]

# Means:

# Row 0 → Column 1

# Row 1 → Column 3

# Row 2 → Column 0

# Row 3 → Column 2

# 2️⃣ is_safe() Function

# Checks constraints before placing queen.

# 🔹 Column Check
# if board[i] == col:

# No two queens in same column.

# 🔹 Diagonal Check
# if abs(board[i] - col) == abs(i - row):

# If absolute difference of rows equals absolute difference of columns → diagonal attack.

# Example:

# (0,0) and (1,1)

# |0−1| = |0−1|

# Same diagonal ❌

# 3️⃣ solve_nqueen()

# Main recursive function.

# Base Case
# if row == n:
#     return True

# All queens placed successfully.

# Try All Columns
# for col in range(n):

# Try placing queen in each column.

# If Safe → Place Queen
# board[row] = col
# Recursive Call
# solve_nqueen(board, row + 1, n)

# Move to next row.

# Backtracking

# If placement fails:

# board[row] = -1

# Remove queen and try next column.

# 4️⃣ print_solution()

# Prints chessboard format:

# Q → Queen

# . → Empty

# Example Output for N=4:

# . Q . .
# . . . Q
# Q . . .
# . . Q .
# 🔁 How Backtracking Works

# Place queen in row 0

# Move to row 1

# If conflict → try next column

# If no column works → go back (backtrack)

# Continue until solution found

# 📊 Time Complexity

# Worst Case:

# 𝑂
# (
# 𝑁
# !
# )
# O(N!)

# Because many combinations are checked.

# 📝 7–8 Mark Exam Answer

# The N-Queen problem is solved using Constraint Satisfaction and Backtracking. Each row is treated as a variable and columns form the domain. The is_safe() function ensures no two queens share the same column or diagonal. The algorithm recursively places queens row by row and backtracks if a conflict occurs.

# 🎯 Why This is CSP?

# Variable → Row

# Domain → Column positions

# Constraints → No column & diagonal conflict

# Search → Backtracking