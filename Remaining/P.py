from queue import Queue

def FIFO(pages,n,capacity):
    s=set()
    indexes=Queue()
    fault=0
    hit=0
    for i in range(n):
        if len(s)<capacity:
            if pages[i] not in s:
                s.add(pages[i])
                indexes.put(pages[i])
                fault+=1
            else:
                hit+=1
        else:
            if pages[i] not in s:
                val=indexes.queue[0]
                s.remove(val)
                indexes.get()
                s.add(pages[i])
                indexes.put(pages[i])
                fault+=1
            else:
            	hit+=1
    print(f"Number of Page Hits: {hit}")
    print(f"Number of Page Faults: {fault}")
    
def LRU(pages,n,capacity):
    s=set()
    indexes={}
    fault=0
    hit=0
    for i in range(n):
        if len(s)<capacity:
            if pages[i] not in s:
                s.add(pages[i])
                fault+=1
            else:
            	hit+=1
            indexes[pages[i]]=i
        else:
            if pages[i] not in s:
                lru=float('inf')
                for page in s:
                    if indexes[page]<lru:
                        lru=indexes[page]
                        val=page
                s.remove(val)
                s.add(pages[i])  
                fault+=1  
            else:
            	hit+=1
            indexes[pages[i]]=i
    print(f"Number of Page Hits: {hit}")
    print(f"Number of Page Faults: {fault}")

def predict(pages,fr,n,index):
    res=-1
    farthest=index
    for i in range(len(fr)):       ###
        j=index
        while(j<n):
            if fr[i]==pages[j]:
                if j>farthest:
                    j=farthest 
                break
            j+=1
        if j==n:
            return i
    return 0 if res==-1 else res
    
def Optimal(pages,n,capacity):
    fr=[]
    fault=0
    hit=0
    for i in range(n):
        if len(fr)<capacity:
            if pages[i] not in fr:
            	fr.append(pages[i])   ####
            	fault+=1
            else:
                hit+=1
        else:
        	if pages[i] not in fr:
        		j=predict(pages, fr, n, i+1)
        		fr[j]=pages[i]
        		fault+=1
        	else:
        		hit+=1
        		
    print("og: ",fault)
    fault=n-hit
    print(f"Number of Page Hits: {hit}")
    print(f"Number of Page Faults: {fault}")

             
def main():
	pages=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
	n=len(pages)
	capacity=3
	print("Total Pages: ",n)
	print("Capacity: ",capacity)
	
	while(True):
		print("Menu\n 1.FIFO\n 2.LRU \n 3.OPTIMAL\n 4.Exit")
		print("Your choice: ")
		ch=int(input())
		if ch==1:
			print("FIFO :")
			FIFO(pages, n, capacity)
			break
		elif ch==2:
			print("LRU :")
			LRU(pages, n, capacity)
			break
		elif ch==3:
			print("Optimal :")
			Optimal(pages, n, capacity)
			break
		elif ch==4:
		    print("Program is quite")
		    break
		else :
			print("Invalid choice.")
			break
    
if __name__=='__main__':
    main()





















