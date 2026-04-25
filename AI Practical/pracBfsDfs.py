from collections import defaultdict, deque

def create_graph(edges):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs(graph, node, visited=None):
    if visited is None:
        visited=set()
    if node not in graph:
        return
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    
    
def bfs(graph, queue, visited):
    if not queue:
        return
    node=queue.popleft()
    if node not in graph:
        return
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    bfs(graph, queue, visited)

def bfs_it(graph, start):
    visited=set()
    queue=deque([start])

    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

edges= [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
graph=create_graph(edges)
print("\nDFS \n")
dfs(graph,0)
start=0
print("\nBFS \n")
bfs(graph,deque([start]),set())
print("\nBFS \n")
bfs_it(graph,0)



