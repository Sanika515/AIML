import heapq

def a_star(graph, start, goal, heuristic):
    pq = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}

    while pq:
        f_cost, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor, cost in graph[node]:
            new_g = g_cost[node] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(pq, (f_cost, neighbor))
                parent[neighbor] = node

    return None


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 3,
    'B': 1,
    'C': 1,
    'D': 0
}

result = a_star(graph, 'A', 'D', heuristic)
print("Optimal Path:", result)