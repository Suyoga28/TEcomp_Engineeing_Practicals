from queue import Queue 

def LRU(pages, n, capacity): 
    s = set() 
    indexes = {} 
    page_faults = 0
    hits = 0
    
    for i in range(n): 
        if len(s) < capacity: 
            if pages[i] not in s: 
                s.add(pages[i]) 
                page_faults += 1
            else:
                hits += 1
            indexes[pages[i]] = i      # 2 times maintain dictionary page:occurence(i.e  int i) 
        else: 
            if pages[i] not in s: 
                lru = float('inf')                      
                for page in s: 
                    if indexes[page] < lru: 
                        lru = indexes[page] 
                        val = page 
                s.remove(val)                 #v
                s.add(pages[i]) 
                page_faults += 1
            else:
                hits += 1
            indexes[pages[i]] = i 
 
    print(f"Number of Page Hits: {hits}")
    print(f"Number of Page Faults: {page_faults}")

'''def search(key, fr):
    for i in range(len(fr)):
        if fr[i] == key:
            return True
    return False
'''
def predict(pages, fr, n, index):
    res = -1
    farthest = index
    for i in range(len(fr)):
        j = index            # i+1
        while j < n:
            if fr[i] == pages[j]:         #finding future page reference k       i is frame and j is for pages so replace i whose j is farthest
                if j > farthest:
                    farthest = j
                    res = i
                break
            j += 1
        if j == n:  # If page not found in future, return this index
            return i
    return 0 if res == -1 else res           # If no farthest page found, return the first

def optimalPage(pages, n, capacity):
    fr = []
    hit = 0
    page_faults = 0

    for i in range(n):
        if len(fr) < capacity:
            if pages[i] not in fr:
                fr.append(pages[i])
            else:
                hit += 1
        else:
            if pages[i] not in fr:
                j = predict(pages, fr, n, i + 1)
                fr[j] = pages[i]    
            else:
                hit += 1
   
            '''if len(fr) < capacity:
                if search(pages[i], fr):
                    hit += 1
                    continue
                else:
                    fr.append(pages[i])
            else:
                if search(pages[i], fr):
                    hit += 1
                    continue
                else:
                    j = predict(pages, fr, n, i + 1)
                    fr[j] = pages[i]'''

    page_faults = n - hit
    print(f"Number of Page Hits: {hit}")
    print(f"Number of Page Faults: {page_faults}")

def FIFO(pages, n, capacity): 
    s = set()
    indexes = Queue() 
    page_faults = 0
    hits = 0

    for i in range(n):  
        if (len(s) < capacity): 
            if (pages[i] not in s): 
                s.add(pages[i])  
                indexes.put(pages[i]) 
                page_faults += 1               
            else:
                hits += 1
        else: 
            if (pages[i] not in s): 
                val = indexes.queue[0]                  
                indexes.get()           # removed value from queue as well
                s.remove(val) 
                s.add(pages[i]) 
                indexes.put(pages[i]) 
                page_faults += 1
            else:
                hits += 1

    print(f"Number of Page Hits: {hits}")
    print(f"Number of Page Faults: {page_faults}")
	
def main():
	print("Paging Simulation program ")
	pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1] 
	n = len(pages) 
	capacity = 3
	#flag=True
	print(f"Total Pages: ",n)
	print(f"Capacity: ",capacity)
	
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
			optimalPage(pages, n, capacity)
			break
		elif ch==4:
		    print("Program is quite")
		    break
		else :
			print("Invalid choice.")
			break
		"""print("Do yo want to continue (y/n)? ")
		choice=input()
		if choice=='N' or choice=='n':
		    flag=False"""
	
if __name__ == '__main__':
    main()
