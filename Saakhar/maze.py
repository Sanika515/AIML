from collections import deque
import heapq

# Maze (0 = free, 1 = blocked)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

rows = len(maze)
cols = len(maze[0])

start = (0, 0)
goal = (4, 4)

# Directions: Up, Down, Left, Right
directions = [(-1,0), (1,0), (0,-1), (0,1)]


# ---------------- BFS ----------------
def bfs():
    queue = deque()
    visited = set()

    queue.append((start, [start]))
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None


# ---------------- DFS ----------------
def dfs():
    stack = []
    visited = set()

    stack.append((start, [start]))
    visited.add(start)

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append(((nx, ny), path + [(nx, ny)]))

    return None


# ---------------- UCS ----------------
def ucs():
    pq = []
    visited = set()

    heapq.heappush(pq, (0, start, [start]))

    while pq:
        cost, (x, y), path = heapq.heappop(pq)

        if (x, y) == goal:
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                    heapq.heappush(pq, (cost + 1, (nx, ny), path + [(nx, ny)]))

    return None


# --------- Run All ---------
print("BFS Path:", bfs())
print("DFS Path:", dfs())
print("UCS Path:", ucs())




# ✔ This is a 5×5 grid.
# ✔ 0 means path is allowed.
# ✔ 1 means blocked.

# 2️⃣ Start and Goal
# start = (0, 0)
# goal = (4, 4)

# These are coordinates (row, column).

# 3️⃣ Directions
# directions = [(-1,0), (1,0), (0,-1), (0,1)]

# This means:

# Movement	Change
# Up	(-1,0)
# Down	(1,0)
# Left	(0,-1)
# Right	(0,1)

# So if current position is (x,y):

# new_x = x + dx
# new_y = y + dy
# 🔵 BFS Explanation
# queue = deque()
# visited = set()

# ✔ Queue → FIFO (First In First Out)
# ✔ Visited → avoids repeating nodes

# Add Start Node
# queue.append((start, [start]))

# We store:

# Current position

# Path taken so far

# Main Loop
# while queue:

# Keep running until queue is empty.

# Remove First Element
# (x, y), path = queue.popleft()

# ✔ BFS removes from front.

# Goal Check
# if (x, y) == goal:
#     return path

# If goal found → return path.

# Explore Neighbors
# for dx, dy in directions:

# Generate new positions.

# Check:

# Inside grid

# Not blocked

# Not visited

# Then:

# queue.append(((nx, ny), path + [(nx, ny)]))

# Add new state to queue.

# Why BFS Finds Shortest Path?

# Because:

# It explores level by level

# First time goal is found → shortest distance

# 🔴 DFS Explanation

# Same logic as BFS but:

# stack = []

# Uses stack instead of queue.

# stack.pop()

# Removes last element (LIFO).

# Difference:
# BFS	DFS
# Queue	Stack
# Level order	Deep first
# Shortest path	Not guaranteed

# DFS may go deep in one direction first.

# 🟢 UCS Explanation
# pq = []
# heapq.heappush(pq, (0, start, [start]))

# ✔ Uses Priority Queue
# ✔ First value = cost

# Remove Smallest Cost
# cost, (x, y), path = heapq.heappop(pq)

# Removes node with minimum cost.

# Add Neighbors
# heapq.heappush(pq, (cost + 1, (nx, ny), path + [(nx, ny)]))

# Here:

# Each move cost = 1

# So cost increases by 1

# Why UCS?

# ✔ Expands lowest cost node first
# ✔ Works best when edge costs are different

# If all costs = 1 → UCS behaves like BFS.

# 🔁 Complete Flow Summary

# Start from initial cell

# Add it to data structure

# Remove one node

# Check if goal

# Expand neighbors

# Repeat until goal found

# 📊 Time Complexity

# Worst Case:

# 𝑂
# (
# 𝑉
# +
# 𝐸
# )
# O(V+E)

# Where:

# V = number of cells

# E = number of connections

# 📝 Viva Answer (Short & Perfect)

# “This program finds a path in a maze using BFS, DFS, and UCS. BFS uses a queue and guarantees the shortest path. DFS uses a stack and explores deeply before backtracking. UCS uses a priority queue and expands the node with minimum cost first. A visited set is used to prevent revisiting nodes.”