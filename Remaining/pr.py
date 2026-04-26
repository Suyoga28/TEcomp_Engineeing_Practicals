def First(BlockSize,m,processSize,n):
    allocation=[-1]*n
    for i in range(n):
        for j in range(m):
            if BlockSize[j]>=processSize[i]:
                allocation[i]=j
                BlockSize[j]-=processSize[i]
                break
    print("Process_No\t\tprocess\t\tBlock_No\t\tRemaing Block_size")
    for i in range(n):
        print(i+1,"\t\t\t",processSize[i],"\t\t\t",end="")
        if allocation[i]!=-1:
            print(allocation[i]+1,"\t\t\t",BlockSize[allocation[i]])            
        else:
            print("Not allocated")

def Next(BlockSize,m,processSize,n):
    allocation=[-1]*n
    j=0
     
    for i in range(n):
        start=j
        while True:
            if BlockSize[j]>=processSize[i]:
                allocation[i]=j
                BlockSize[j]-=processSize[i]
                break
            j=(j+1)%m
            if j==start:
                break
    print("Process_No\t\tprocess\t\tBlock_No\t\tRemaing Block_size")
    for i in range(n):
        print(i+1,"\t\t\t",processSize[i],"\t\t\t",end="")
        if allocation[i]!=-1:
            print(allocation[i]+1,"\t\t\t",BlockSize[allocation[i]])            
        else:
            print("Not allocated")

def Best(BlockSize,m,processSize,n):
    allocation=[-1]*n
    for i in range(n):
        BstIdx=-1
        for j in range(m):
            if BlockSize[j]>=processSize[i]:
                if BstIdx==-1 or BlockSize[BstIdx]>BlockSize[j]:
                    BstIdx=j
        if BstIdx!=-1:
            allocation[i]=BstIdx
            BlockSize[BstIdx]-=processSize[i]
    print("Process_No\t\tprocess\t\tBlock_No\t\tRemaing Block_size")
    for i in range(n):
        print(i+1,"\t\t\t",processSize[i],"\t\t\t",end="")
        if allocation[i]!=-1:
            print(allocation[i]+1,"\t\t\t",BlockSize[allocation[i]])            
        else:
            print("Not allocated")          
     

def Worst(BlockSize,m,processSize,n):
    allocation=[-1]*n
    for i in range(n):
        WstIdx=-1
        for j in range(m):
            if BlockSize[j]>=processSize[i]:
                if WstIdx==-1 or BlockSize[WstIdx]<BlockSize[j]:
                    WstIdx=j
        if WstIdx!=-1:
            allocation[i]=WstIdx
            BlockSize[WstIdx]-=processSize[i]
    print("Process_No\t\tprocess\t\tBlock_No\t\tRemaing Block_size")
    for i in range(n):
        print(i+1,"\t\t\t",processSize[i],"\t\t\t",end="")
        if allocation[i]!=-1:
            print(allocation[i]+1,"\t\t\t",BlockSize[allocation[i]])            
        else:
            print("Not allocated")   

def main():
    BlockSize1=[100, 500, 200, 300, 600]
    processSize1=[212, 417, 112, 426]
    BlockSize2=[100, 500, 200, 300, 600]
    processSize2=[212, 417, 112, 426]
    BlockSize3=[100, 500, 200, 300, 600]
    processSize3=[212, 417, 112, 426]
    BlockSize4=[100, 500, 200, 300, 600]
    processSize4=[212, 417, 112, 426]
    
    m=len(BlockSize1)
    n=len(processSize1)
    
    print("First Fit Allocation")
    First(BlockSize1,m,processSize1,n)
    print("Next Fit Allocation")
    Next(BlockSize2,m,processSize2,n)
    print("Best Fit Allocation")
    Best(BlockSize3,m,processSize3,n)
    print("Worst Fit Allocation")
    Worst(BlockSize4,m,processSize4,n)

if __name__ =="__main__":
    main()
