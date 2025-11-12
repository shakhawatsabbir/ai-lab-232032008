from collections import deque

def BFS(graph, st_node):
    VISITED = set()  
    queue = deque()  
    queue.append(st_node)
    VISITED.add(st_node)
    traversal_order = [] 
    while queue:
        CT_NODE = queue.popleft()   
        traversal_order.append(CT_NODE)
        for NEIGHBOR in graph.get(CT_NODE, []): 
            if NEIGHBOR not in VISITED:
                VISITED.add(NEIGHBOR)
                queue.append(NEIGHBOR)
    return traversal_order
 
if __name__ == "__main__": 
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F','G'],
        'D' : [],
        'E' : [],
        'F' : [],
        'G' : ['H','I'],
        'I' : ['J'],
        'J': []
    }

    st_node = 'A'
    BFS_result = BFS(graph, st_node)
    print(f"BFS traversal starting from '{st_node}': {BFS_result}")
