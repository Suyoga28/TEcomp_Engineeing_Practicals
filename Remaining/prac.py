def fcfs(processes):
    result=[]
    time=0
    print("fcfs scheduling\n")
    for pid, at, bt in sorted(processes, key=lambda x:x[1]):
        start_time = max(at,time)
        end_time = start_time+bt
        time=end_time
        result.append((pid, end_time-at))
        print(f"Process {pid} executed from {start_time} to {end_time}")
    return result
    
def prior(processes):
    result=[]
    time=0
    print("fcfs scheduling\n")
    for pid, at, bt ,pr in sorted(processes, key=lambda x:(x[1],x[3])):
        start_time = max(at,time)
        end_time = start_time+bt
        time=end_time
        result.append((pid, end_time-at))
        print(f"Process {pid} executed from {start_time} to {end_time}")
    return result

def rr(processes,quantum):
    time,queue,result,wait=0,processes[:],[],{p[0]:0 for p in processes}
    print("RR Scheduling\n")
    while queue:
        pid,at,bt=queue.pop(0)
        if time<at:
            time=at
        exec_time=min(bt,quantum)
        print(f"Process {pid} executed from {time} to {time+exec_time}") 
        time+=exec_time
        bt-=exec_time
        if bt>0:
            queue.append((pid,at,bt))
        else:
            wait[pid]=time-at
    return [(p,wait[p])for p in wait]
       
def srjf(processes):
    time,queue,result=0,[],[]
    print("srjf Scheduling\n")
    while processes or queue:
        queue+= [(pid,at,bt) for pid,at,bt in processes if at<=time]
        processes= [(pid,at,bt) for pid,at,bt in processes if at>time]
        if queue:
        	pid,at,bt=min(queue, key=lambda x:x[2])
        	queue.remove((pid,at,bt))
        	exec_time=1
        	print(f"Process {pid} executed from {time} to {time+exec_time}") 
        	time+=exec_time
        	bt-=exec_time
        	if bt>0:
        		queue.append((pid,at,bt))
        	else:
        		result.append((pid,time-at))
        else:
        	time+=1        
    return result
    
def main():
    print("CPU Scheduling Simulator")
    print("1. FCFS Scheduling")
    print("2. Round Robin Scheduling")
    print("3. SJF Scheduling (Preemptive)")
    print("4. Priority Scheduling (Non-Preemptive)")
    
    choice = int(input("Enter your choice: "))
    n = int(input("Enter number of processes: "))
    processes = []
    
    for i in range(n):
        pid = int(input("Process ID: "))
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        if choice == 4:
            pr = int(input("Priority: "))
            processes.append((pid, at, bt, pr))
        else:
            processes.append((pid, at, bt))
    
    if choice == 1:
        result = fcfs(processes)
    elif choice == 2:
        quantum = int(input("Enter quantum time for Round Robin: "))
        result = rr(processes, quantum)
    elif choice == 3:
        result = srjf(processes)
    elif choice == 4:
        result = prior(processes)
    else:
        print("Invalid choice.")
        return
    
    print("Result:", result)

if __name__ == "__main__":
    main()







































