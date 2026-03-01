from collections import deque

# Goal State
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate new states
def generate_moves(state):
    moves = []
    x, y = find_blank(state)

    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            moves.append(new_state)

    return moves

# BFS Algorithm
def bfs(start_state):
    queue = deque()
    visited = set()

    queue.append((start_state, []))
    visited.add(str(start_state))

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        for move in generate_moves(current_state):
            if str(move) not in visited:
                visited.add(str(move))
                queue.append((move, path + [current_state]))

    return None


# Initial State
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = bfs(start_state)

if solution:
    print("Solution found!\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")

#     1️⃣ Goal State
# goal_state = [...]

# This is the final configuration we want to reach.

# 2️⃣ find_blank(state)

# Finds position of 0 (blank tile).

# Returns row and column.

# 3️⃣ generate_moves(state)

# Generates all valid next states.

# Steps:

# Find blank

# Try moving:

# Up

# Down

# Left

# Right

# If move valid → create new state

# Add to move list

# This represents state expansion.

# 4️⃣ BFS Algorithm
# Initialize:
# queue = deque()
# visited = set()

# Queue → stores states

# Visited → avoids revisiting states

# Add Start State
# queue.append((start_state, []))

# Stores:

# Current state

# Path taken

# Main Loop
# while queue:

# Remove first state (FIFO)

# Check if goal

# Generate neighbors

# Add new states to queue

# Why BFS Works?

# Because:

# It explores level by level

# First time goal is found → shortest path

# 📊 State Space Concept
#         Start
#        /  |   \
#      S1   S2   S3
#      /          \
#    S4            Goal

# Each node = board configuration.

# 📝 Exam Theory (Short Answer)

# The 8-Puzzle problem is solved using State Space Search where each configuration is treated as a state. BFS is used to explore states level by level. At each step, possible moves of the blank tile are generated. A visited set prevents repeated states. BFS guarantees the shortest path to the goal state.

# ⏱ Time & Space Complexity

# Worst Case:

# 𝑂
# (
# 𝑏
# 𝑑
# )
# O(b
# d
# )

# Where:

# b = branching factor (max 4)

# d = depth of solution