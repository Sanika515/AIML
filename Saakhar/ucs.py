import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [])]   # (cost, current_node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return cost, path + [node]

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, neighbor, path + [node]))

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('D', 1)],
    'D': [],
    'E': []
}

result = ucs(graph, 'A', 'D')
print("Least Cost:", result[0])
print("Path:", result[1])