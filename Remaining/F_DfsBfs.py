#If u is not in the graph yet, it automatically creates an empty list for graph[u], so no need to check if the key exists.
from collections import defaultdict, deque  

def create_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Since it's an undirected graph
    return graph

# Depth-First Search (Recursive)
def dfs(graph, node, visited=None):
    if node not in graph:
        return
    
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    
            
def bfs_recursive( graph, queue, visited):
    if not queue:
        return

    node = queue.popleft()
    if node not in graph:
        return

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    bfs_recursive( graph, queue, visited)


# Breadth-First Search (Iterative)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
def dfs_iterative(graph, start):
    if start not in graph:
        return
    
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors in reverse order for natural left-to-right traversal
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph represented as edge list
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
graph = create_graph(edges)

print("Recursive DFS Traversal:")
dfs(graph, 0)
print("\nRecursive BFS Traversal:")
start = 0
bfs_recursive( graph, deque([start]), set())
print("\nIterative BFS Traversal:")
bfs(graph, 0)
