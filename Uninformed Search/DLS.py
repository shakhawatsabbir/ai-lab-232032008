def DLS(graph, start, goal, limit):
    def DLS_recursive(node, depth):
        if node == goal:
            return 'success'
        elif depth == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for neighbor in graph.get(node, []):
                result = DLS_recursive(neighbor, depth - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result != 'fail':
                    return result  
            if cutoff_occurred:
                return 'cutoff'
            else:
                return 'fail'
    return DLS_recursive(start, limit)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

start_node = 'A'
goal_node = 'H'
depth_limit = 3
result = DLS(graph, start_node, goal_node, depth_limit)
print(f"Search result for goal '{goal_node}' with limit {depth_limit}: {result}")
depth_limit_fail = 2
fail_result = DLS(graph, start_node, goal_node, depth_limit_fail)
print(f"Search result for goal '{goal_node}' with limit {depth_limit_fail}: {fail_result}")

goal_node_not_exist = 'Z'
result_not_exist = DLS(graph, start_node, goal_node_not_exist, depth_limit)
print(f"Search result for goal '{goal_node_not_exist}' with limit {depth_limit}: {result_not_exist}")
