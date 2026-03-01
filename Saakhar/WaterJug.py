from collections import deque

# Jug capacities
jug1 = 4
jug2 = 3
goal = 2

def water_jug():
    
    visited = set()
    queue = deque()
    
    # Start from (0,0)
    queue.append((0, 0, []))
    
    while queue:
        x, y, path = queue.popleft()
        
        # If goal reached
        if x == goal or y == goal:
            path.append((x, y))
            return path
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        # Possible operations
        
        next_states = [
            (jug1, y),          # Fill Jug1
            (x, jug2),          # Fill Jug2
            (0, y),             # Empty Jug1
            (x, 0),             # Empty Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug1 -> Jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug2 -> Jug1
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path + [(x, y)]))
    
    return None


solution = water_jug()

if solution:
    print("Solution Path:")
    for step in solution:
        print(step)
else:
    print("No solution found")