# Graph as a dictionary
graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

# Heuristic values
heuristics = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

# Print the graph structure with costs and heuristic values
for node in graph:
    neighbors = graph[node]
    heuristic_value = heuristics[node]
    print(f"Node: {node}, Heuristic: {heuristic_value}")

    for neighbor, cost in neighbors.items():
        print(f"  Neighbor: {neighbor}, Cost: {cost}")

    print()
