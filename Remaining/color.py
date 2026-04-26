def is_safe(graph,node,color,colors):
	for neighbor in graph[node]:
		if colors[neighbor]==color:
			return False
	return True	

def bound(graph,m,node,colors):
	for i in range(node,len(graph)):
		available_colors=set(range(1,m+1))
		for neighbor in graph[i]:
		    if colors[neighbor] in available_colors:
		        available_colors.remove(colors[neighbor])
		if len(available_colors)==0:
			return False
	return True


def graph_coloring(graph,m,node,colors):
	if node==len(graph):
		return True
	if not bound(graph,m,node,colors):
		return False
	for color in range(1,m+1):
		if is_safe(graph,node,color,colors):
			colors[node]=color
			if graph_coloring(graph,m,node+1,colors):
				return True
			colors[node]=0
	return False

def main(graph,m):
	n=len(graph)
	colors= [0]*n
	
	color_names={
		1:"Red",
		2:"Blue",
		3:"Green",
		4:"Yellow",
		5:"Pink"
	}
	
	if graph_coloring(graph,m,0,colors):
		print("\nSolution found!\n",colors)
		named_colors=[color_names.get(c,f"Color{c}") for c in colors]
		print(named_colors)
	else:
		print("\nSolution not exists")

graph={
	0:[1,2],
	1:[0,2,3],
	2:[0,1,3],
	3:[1,2]
}
m=3
main(graph,m)
