def prim(graph, start):  #Adjacency list {'A': [('B', 3), ('C', 5)]}
    visited = set()
    mst = []
    while len(visited) < len(graph):
        min_edge = None
        for u in visited or [start]:    #u = 'A' v = 'B' w = 5
            for v, w in graph[u]:
                if v not in visited:
                    if min_edge is None or w < min_edge[2]:
                        min_edge = (u, v, w)
        if min_edge:
            u, v, w = min_edge
            visited.add(v)
            mst.append((u, v, w))
    return mst

def kruskal(edges, nodes):
    parent = {n: n for n in nodes}
    def find(n):
        while parent[n] != n:
            n = parent[n]
        return n

    mst = []
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        ru, rv = find(u), find(v)   #Only edges that do not form a cycle are added.
        if ru != rv:                   #Components (trees) are merged when an edge is added.
            parent[rv] = ru
            mst.append((u, v, w))
    return mst

if __name__== "__main__":
    n = int(input("How many edges? "))
    edges = []
    graph = {}

    print("Enter edges like: A B 3")
    for i in range(n):
        u, v, w = input().split()
        w = int(w)
        edges.append((u, v, w))
        for a, b in [(u, v), (v, u)]:
            if a not in graph:
                graph[a] = []
            graph[a].append((b, w))

    nodes = set(graph.keys())
    start_node = input("Start node for Prim's: ")

    print("\nPrim's MST:")
    for u, v, w in prim(graph, start_node):
        print(f"{u} - {v} ({w})")

    print("\nKruskal's MST:")
    for u, v, w in kruskal(edges, nodes):
        print(f"{u} - {v} ({w})")
