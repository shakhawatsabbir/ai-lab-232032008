def DFS_recursive(graph, node, visited):
    visited.add(node)
    print(node, end=" ")   
    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS_recursive(graph, neighbor, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited_nodes = set()
print("DFS Traversal (Recursive):")
DFS_recursive(graph, 'A', visited_nodes)
