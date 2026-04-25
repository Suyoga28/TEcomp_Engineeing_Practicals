#Prims Algo
import heapq

def prim(graph, start):
    mst, visited, edges = [], set(), [(0, start, None)]
    
    while edges:
        cost, node, parent = heapq.heappop(edges)
        if node not in visited:
            visited.add(node)
            if parent: mst.append((parent, node, cost))
            for neighbor, weight in graph[node].items():
                heapq.heappush(edges, (weight, neighbor, node))
    
    return mst
# Graph (Adjacency List)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'D': 3, 'F': 5},
    'D': {'B': 2, 'C': 3, 'E': 6},
    'E': {'D': 6, 'F': 2},
    'F': {'C': 5, 'E': 2}
}

print("Prim's MST:", prim(graph, 'A'))

#Kruskal Algo
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  # Path compression
    return parent[node]

def union(parent, rank, u, v):
    root1, root2 = find(parent, u), find(parent, v)
    if root1 != root2:
        if rank[root1] > rank[root2]: parent[root2] = root1
        else: parent[root1] = root2
        if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(edges, nodes):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    parent, rank = {n: n for n in nodes}, {n: 0 for n in nodes}
    mst = []

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
    return mst

# Graph (Edge List)
edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'D', 2), ('C', 'D', 3), ('C', 'F', 5), ('D', 'E', 6), ('E', 'F', 2)]
nodes = {'A', 'B', 'C', 'D', 'E', 'F'}

print("Kruskal's MST:", kruskal(edges, nodes))
