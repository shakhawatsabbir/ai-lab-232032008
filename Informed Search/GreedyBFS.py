import heapq
def GBFS(graph, start, goal, heuristic):
    priority_queue = [] 
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()
    path = {start: None}  
    while priority_queue:
        current_h_value, current_node = heapq.heappop(priority_queue)
        if current_node == goal:
            return reconstruct_path(path, start, goal)
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                path[neighbor] = current_node  
    return None  
def reconstruct_path(path_map, start, goal): 
    current = goal
    path = []
    while current is not None:
        path.append(current)
        current = path_map.get(current)
    return path[::-1] 
if __name__ == "__main__": 
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }
    heuristic = { 'A': 10, 'B': 7, 'C': 8, 'D': 4, 'E': 3, 'F': 2, 'G': 0 }
    start_node = 'A'
    goal_node = 'G'
    found_path = GBFS(graph, start_node, goal_node, heuristic)
    if found_path:
        print(f"Path from {start_node} to {goal_node}: {found_path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
