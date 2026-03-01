import random

# Distance matrix (example with 4 cities)
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(distance)


# Calculate total distance of tour
def calculate_cost(route):
    total = 0
    for i in range(n - 1):
        total += distance[route[i]][route[i+1]]
    total += distance[route[-1]][route[0]]  # return to start
    return total


# Hill Climbing Algorithm
def hill_climbing():
    
    # Initial random route
    current_route = list(range(n))
    random.shuffle(current_route)
    
    current_cost = calculate_cost(current_route)
    
    improved = True
    
    while improved:
        improved = False
        
        for i in range(n):
            for j in range(i+1, n):
                
                # Create new neighbor by swapping two cities
                new_route = current_route[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]
                
                new_cost = calculate_cost(new_route)
                
                # If better solution found
                if new_cost < current_cost:
                    current_route = new_route
                    current_cost = new_cost
                    improved = True
        
    return current_route, current_cost


# Run algorithm
best_route, best_cost = hill_climbing()

print("Best Route:", best_route)
print("Minimum Cost:", best_cost)

# Travelling Salesman Problem (TSP)

# Goal:

# A salesman must visit all cities exactly once and return to starting city with minimum total distance.

# This is an Optimization Problem.

# 🧠 Why Hill Climbing?

# Hill Climbing:

# Starts with a random solution

# Makes small changes (neighbors)

# Moves to better solution

# Stops when no better neighbor found

# This is called Local Search.
# Distance Matrix
# distance = [...]

# Represents distances between cities.

# Example:
# Distance from city 0 to city 1 = 10

# 2️⃣ calculate_cost(route)

# Calculates total distance of route.

# Example route:

# [0, 2, 3, 1]

# It calculates:

# 0 → 2
# 2 → 3
# 3 → 1
# 1 → 0 (return)

# 3️⃣ Initial Solution
# current_route = list(range(n))
# random.shuffle(current_route)

# Generates random route.

# Example:

# [2, 0, 3, 1]
# 4️⃣ Generate Neighbor
# new_route[i], new_route[j] = new_route[j], new_route[i]

# Swap two cities.

# Example:
# Before: [0, 1, 2, 3]
# After swap(1,3): [0, 3, 2, 1]

# This is called neighbor solution.

# 5️⃣ Improvement Check
# if new_cost < current_cost:

# If new route is better:

# Accept it

# Continue searching

# 6️⃣ Stop Condition

# If no better neighbor found → stop.

# This is called Local Optimum.

# 🔄 Hill Climbing Flow

# Start with random solution

# Generate neighbor

# If better → move there

# Repeat

# Stop when no improvement

# 📊 Example Output
# Best Route: [0, 1, 3, 2]
# Minimum Cost: 80
# ⚠ Limitation

# Hill Climbing may get stuck in Local Minimum.

# It does not guarantee global optimal solution.

# 📝 7–8 Mark Exam Answer

# The Travelling Salesman Problem is solved using Hill Climbing, a local search technique. A random tour is generated initially. Neighbor solutions are created by swapping two cities. If a neighbor has lower cost, it replaces the current solution. The process continues until no better neighbor is found. The algorithm stops at a local optimum.

# 📌 Time Complexity

# Each iteration:

# 𝑂
# (
# 𝑛
# 2
# )
# O(n
# 2
# )

# Total depends on number of improvements.

# 🎯 Why This is Optimization?

# Because we try to minimize:

# 𝑇
# 𝑜
# 𝑡
# 𝑎
# 𝑙
 
# 𝐷
# 𝑖
# 𝑠
# 𝑡
# 𝑎
# 𝑛
# 𝑐
# 𝑒
# Total Distance