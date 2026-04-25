def is_safe(graph, node, color, colors): 
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

# Bounding function to check if further coloring is possible
def bound(graph, m, node, colors):
    """Return True if colors left for the remaining nodes."""
    for i in range(node, len(graph)):
        available_colors = set(range(1, m + 1))
        for neighbor in graph[i]:
            if colors[neighbor] in available_colors:
                available_colors.remove(colors[neighbor])
        if len(available_colors) == 0:
            return False 
    return True

def graph_coloring(graph, m, node, colors):
    """Recursive function to solve graph coloring using Backtracking + Branch and Bound."""
    if node == len(graph):
        return True  # All nodes are colored successfully
    
    if not bound(graph, m, node, colors):  # Use branch and bound to prune search space
        return False  # Prune the branch if no valid coloring is possible

    for color in range(1, m + 1):   # Try all colors for the current node
        if is_safe(graph, node, color, colors):
            colors[node] = color
            if graph_coloring(graph, m, node + 1, colors):  # Recur to color the next node
                return True
            colors[node] = 0  # Backtrack if the color assignment didn't work
    return False  # No solution found for this node

def main_gcoloring(graph, m):
    n = len(graph)
    colors = [0] * n  # Initialize all nodes with color 0 (uncolored)

    color_names = {
        1: "Red",
        2: "Green",
        3: "Blue",
        4: "Yellow",
        5: "Orange",
        6: "Purple"
    }

    if graph_coloring(graph, m, 0, colors):
        print("Solution Found! Node color numbers:", colors)
        named_colors = [color_names.get(c, f"Color{c}") for c in colors]
        print("Node color names:", named_colors)
    else:
        print("No solution exists for the given number of colors.")

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]       }

m = 3  # Number of colors
main_gcoloring(graph, m)
