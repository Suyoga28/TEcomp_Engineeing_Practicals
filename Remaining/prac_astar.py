from queue import PriorityQueue

def astar(graph,start,goal,heuristic):
	oplist=PriorityQueue()
	oplist.put((0,start))
	came_from={}
	g_score={node:float('inf') for node in graph}
	g_score[start]=0
	
	while not oplist.empty():
		f_score,current=oplist.get()
		print(f_score,current)
		
		if (current==goal):
			path=[]
			while current in came_from:
				path.append(current)
				current=came_from[current]
			path.append(start)
			return path[::-1]	
	
		for neighbor, cost in graph[current].items():
			temp_g_score= g_score[current]+cost
			if temp_g_score < g_score[neighbor]:
				came_from[neighbor]=current
				g_score[neighbor]=temp_g_score
				f_score= temp_g_score + heuristic[neighbor]
				oplist.put((f_score, neighbor))
			
	return None
	
graph={
        'A':{'B':1,'C':4},
        'B':{'D':2},
        'C':{'F':3},
        'D':{'F':4},
        'F':{'E':2},
        'E':{}
}

heuristic={'A':7,'B':6,'C':2,'D':3,'E':0,'F':1}

path=astar(graph,'A','E',heuristic)
if path:
    print("Shortetst path = ","->".join(path))
else:
    print("Path not found")	
	
	
	
	
	
	
	
	
	
	
	
