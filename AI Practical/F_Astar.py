from queue import PriorityQueue  #cause lowest estimated total cost

def a_star(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0, start))  #start node with f(n) = 0
    came_from = {}  # track of the most efficient previous node for each visited node, for path reconstruction.
    g_score = {node: float('inf') for node in graph}  #Initializes cost from start to every other node infinity, except start node -> new_dict = {key_expression: value_expression for item in iterable}
    g_score[start] = 0
    
    while not open_list.empty():
        f_score, current = open_list.get()
        print(f"Exploring: {current} with f(n) = {f_score}")
        
        #Checks if the goal has been reached and reconstructs the path from the start node to the goal.
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  #from start to goal
        
        #Examines each neighbor of the current node to determine if a shorter path to that neighbor exists through the current node.
        for neighbor, cost in graph[current].items():   #for key, value in some_dict.items():
            temp_g_score = g_score[current] + cost
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score = temp_g_score + heuristic[neighbor] #Ensure clarity of f(n)
                open_list.put((f_score, neighbor))# Adds neighbor to the open list with its f(n) as the priority
    return None 

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'F': 3},
    'D': {'F': 4},   
    'F': {'E': 2},   
    'E': {}
}

heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 3, 'E': 0, 'F': 1}  # Estimated cost to goal (E)

path = a_star(graph, 'A', 'E', heuristic)
if path:
    print("Shortest Path:", " → ".join(path))
else:
    print("No path found.")