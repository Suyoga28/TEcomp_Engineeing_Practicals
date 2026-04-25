def is_safe(graph, node, color, colors):
    """Check if the current node can be assigned the given color."""
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, m, node, colors):
    """Recursive function to solve graph coloring using backtracking."""
    if node == len(graph):
        return True  # All nodes are colored successfully

    for c in range(1, m + 1):
        if is_safe(graph, node, c, colors):
            colors[node] = c  # Assign color
            if graph_coloring(graph, m, node + 1, colors):
                return True
            colors[node] = 0  # Backtrack

    return False

def solve_graph_coloring(graph, m):
    """Main function to start the coloring process."""
    n = len(graph)
    colors = [0] * n  # Initialize all nodes with color 0 (uncolored)

    if graph_coloring(graph, m, 0, colors):
        print("Solution Exists! Node colors:", colors)
    else:
        print("No solution exists for the given number of colors.")

# Example Graph (Adjacency List Representation)
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

m = 3  # Number of colors
solve_graph_coloring(graph, m)
