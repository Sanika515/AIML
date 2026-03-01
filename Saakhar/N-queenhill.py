import random

# Count number of conflicts
def conflicts(state):
    n = len(state)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                count += 1
    return count


def hill_climbing(n):
    # Random initial state
    state = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        current_conflicts = conflicts(state)
        if current_conflicts == 0:
            return state

        best_state = state
        best_conflicts = current_conflicts

        # Generate neighbors
        for row in range(n):
            for col in range(n):
                new_state = state[:]
                new_state[row] = col
                new_conflicts = conflicts(new_state)

                if new_conflicts < best_conflicts:
                    best_state = new_state
                    best_conflicts = new_conflicts

        if best_conflicts >= current_conflicts:
            return "Stuck in Local Minimum"

        state = best_state


n = 4
result = hill_climbing(n)
print("Solution:", result)



# 🔷 Why It Is Called Hill Climbing?

# Think like climbing a hill:

# Current position = current solution

# Neighbor = small change

# Move to better neighbor

# Stop when no higher hill

# 🔷 Important Concept

# Hill Climbing:

# Fast

# Memory efficient

# May get stuck in local minimum

# Not guaranteed to find solution