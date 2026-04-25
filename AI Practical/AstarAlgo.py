def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def astar(grid, start, goal):
    open_list = [start]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        current = min(open_list, key=lambda x: g_score.get(x, float('inf')) + heuristic(x, goal))

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_list.remove(current)

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:  # right, down, left, up
            neighbor = (current[0]+dx, current[1]+dy)

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue  # obstacle
                temp_g = g_score[current] + 1
                if temp_g < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = temp_g
                    came_from[neighbor] = current
                    if neighbor not in open_list:
                        open_list.append(neighbor)
    return None  # No path

grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]

start = (0,0)
goal = (2,0)

path = astar(grid, start, goal)
print("Path:", path)
