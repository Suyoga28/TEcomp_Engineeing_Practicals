def prims(graph, start):
    visited=set()
    mst=[]

    while len(visited)<len(graph):
	    min_edge=None
	    for u in visited or [start]:
	        for v,w in graph[u]:
	    	    if v not in visited:
	    		    if min_edge is None or w<min_edge[2]:
	    			    min_edge = (u,v,w)
	    if(min_edge):
		    (u,v,w)=min_edge
		    visited.add(v)
		    mst.append((u,v,w))	
    return mst
    
def kruskals(edges,nodes):
	mst=[]
	parent={n:n for n in graph}
	def find(n):
	    while parent[n]!=n:
	        n=parent[n]
	    return n
	    
	for u,v,w in sorted(edges,key=lambda x: x[2]):
	    ru,rv=find(u),find(v)
	    if ru!=rv:
	        parent[rv]=ru
	        mst.append((u,v,w))
	return mst


if __name__=="__main__":
	n=int(input("How many edges?"))
	edges=[]
	graph={}
	
	print("Enter edges like- A B 3")
	for i in range (n):
		u,v,w=input().split()
		edges.append((u,v,w))
		for a,b in [(u,v),(v,u)]:
		    if a not in graph:
		    	graph[a]=[]
		    graph[a].append((b,w))
		    
	
	nodes=set(graph.keys())
	start_node=input("\nEnter start node for prims: ")
	
	print("\nPrims Algo")
	for u,v,w in prims(graph,start_node):
	    print(f"{u}-{v}  ({w})")
		
	print("\nKruskal's Algo")
	for u,v,w in kruskals(edges,nodes):
	    print(f"{u}-{v}  ({w})")
	    

		
		
		
		
		
		
		
		
		
		
		
		
