def dls(tree, node, goal, depth_limit):
    if depth_limit < 0:
        return False

    if node == goal:
        return True

    for child in tree.get(node, []):
        if dls(tree, child, goal, depth_limit - 1):
            return True

    return False


def iddfs(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        if dls(tree, start, goal, depth):
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
max_depth = 3

result = iddfs(tree, start, goal, max_depth)

print("Goal Found:", result)