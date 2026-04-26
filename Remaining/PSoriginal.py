# set= add,remove
# queue= put,get
# dictionary= indexes[pages[i]] that number   indexes[page] occurence of that num  

from queue import Queue

def FIFO(pages, n, capacity):
    s= set()
    indexes= Queue()               #
    fault=0
    hit=0
    
    for i in range(n):
        if (len(s)<capacity):
            if (pages[i] not in (s)):
                s.add(pages[i])
                indexes.put(pages[i])        # if new page is added then 2 times maintain queue and it to q also
                fault+=1
            else:
                hit+=1
        else:
            if (pages[i] not in (s)):
                val=indexes.queue[0]      #small q
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                fault+=1
            else:
                hit+=1
    print("Number of Page Faults: ",fault)
    print("Number of Page Hits: ",hit)
    
def LRU(pages, n, capacity):    
    s=set()
    indexes={}
    fault=0
    hit=0
    
    for i in range(n):
        if (len(s)< capacity):
            if (pages[i] not in s):
                s.add(pages[i])
                fault+=1
            else:
                hit+=1
            indexes[pages[i]]=i    # that number
        else:
            if (pages[i] not in s):
                lru=float('inf')             #infinity
                for page in s:               # we need to store lru from old frames to remaove page
                    if indexes[page]<lru:    # occurence of that num
                        lru=indexes[page]
                        val=page
                s.remove(val)
                s.add(pages[i])
                fault+=1    
            else:
                hit+=1
            indexes[pages[i]]=i
    print("Number of Page Faults: ",fault)
    print("Number of Page Hits: ",hit)

def search(key, fr):
    for i in range (len(fr)):
        if (fr[i]==key):
            return True
    return False
    
def predict(pages, n, fr, index):
    res=-1
    farthest=index
    for i in range (len(fr)):
        j=index                        # IMP
        while(j<n):
            if (fr[i]==pages[j]):    #
                if (farthest < j):
                    farthest=j
                    res=i
                break    
            j+=1             
        if(j==n):
            return i   
    return 0 if res==-1 else res 
 
def OPTIMAL(pages, n, capacity):
    fault=0
    totalfault=0
    hit=0
    fr=[]
    for i in range(n):
        if (len(fr) < capacity):
            if (search(pages[i], fr)):
                hit+=1
                continue
            else:    
                fr.append(pages[i])
                fault+=1
        else:
            if (search(pages[i], fr)):
                hit+=1
                continue
            else:    
                j=predict(pages, n, fr, i+1)
                fr[j]=pages[i] 
                fault+=1
                
    totalfault=n-hit
    print("total fault",totalfault)
    print("Number of Page Faults: ",fault)
    print("Number of Page Hits: ",hit)
    
pages=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
n=len(pages)
capacity=3

print(" Pages- ", pages)
print(" Total number of pages- ",n )
print(" Frame capacity- ", capacity)
print("FIFO :")
FIFO(pages, n, capacity)
print("LRU :")
LRU(pages, n, capacity)
print("OPTIMAL :")
OPTIMAL(pages, n, capacity)
