def dls(tree, node, goal, depth_limit):
    if depth_limit < 0:
        return False

    if node == goal:
        return True

    for child in tree.get(node, []):
        if dls(tree, child, goal, depth_limit - 1):
            return True

    return False


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start = 'A'
goal = 'E'
depth_limit = 2

result = dls(tree, start, goal, depth_limit)

print("Target Found:", result)