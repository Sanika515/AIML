def dfs(graph, node, visited, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True   # Cycle detected

    return False


graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

visited = set()
has_cycle = dfs(graph, 1, visited, -1)

print("Visited Nodes:", visited)
print("Cycle Detected:", has_cycle)