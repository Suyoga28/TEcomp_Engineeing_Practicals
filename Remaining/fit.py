class SimpleMemoryAllocator:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks       #Initialize memory with given blocks.

    def first_fit(self, request_size):
        for i in range(len(self.memory_blocks)):
            if self.memory_blocks[i] >= request_size:
                self.memory_blocks[i] -= request_size
                return f"Allocated {request_size} units using First Fit."
        return "No suitable block found for First Fit."

    def best_fit(self, request_size):
        best_index = -1
        for i in range(len(self.memory_blocks)):
            if self.memory_blocks[i] >= request_size:
                if best_index == -1 or self.memory_blocks[i] < self.memory_blocks[best_index]:     #searching best index
                    best_index = i
        if best_index != -1:
            self.memory_blocks[best_index] -= request_size
            return f"Allocated {request_size} units using Best Fit."
        return "No suitable block found for Best Fit."

    def worst_fit(self, request_size):
        worst_index = -1
        for i in range(len(self.memory_blocks)):
            if self.memory_blocks[i] >= request_size:
                if worst_index == -1 or self.memory_blocks[i] > self.memory_blocks[worst_index]:
                    worst_index = i
        if worst_index != -1:
            self.memory_blocks[worst_index] -= request_size
            return f"Allocated {request_size} units using Worst Fit."
        return "No suitable block found for Worst Fit."

    def next_fit(self, request_size):
        if not hasattr(self, 'last_index'):   #run if false
            self.last_index = 0

        for i in range(len(self.memory_blocks)):
            index = (self.last_index + i) % len(self.memory_blocks)
            if self.memory_blocks[index] >= request_size:
                self.memory_blocks[index] -= request_size
                self.last_index = index  # Update last index
                return f"Allocated {request_size} units using Next Fit."
        return "No suitable block found for Next Fit."


def main():
    memory_blocks = [100, 500, 200, 300, 600]        # Initial memory blocks
    requests = [212, 417, 112, 426]      # Memory request sizes

    allocator = SimpleMemoryAllocator(memory_blocks)
    print("First fit : ")
    for request in requests:
        print(allocator.first_fit(request)) 
    print("Remaining Memory Blocks:")
    print(allocator.memory_blocks,"\n")   # Test First Fit
    
    print("Best fit : ")
    for request in requests:   
        print(allocator.best_fit(request)) 
    print("Remaining Memory Blocks:")
    print(allocator.memory_blocks,"\n")    # Test Best Fit
    
    print("Worst fit : ")
    for request in requests:   
        print(allocator.worst_fit(request))
    print("Remaining Memory Blocks:")
    print(allocator.memory_blocks,"\n")    # Test Worst Fit
    
    print("Next fit : ")
    for request in requests:   
        print(allocator.next_fit(request))     # Test Next Fit
    print("Remaining Memory Blocks:")
    print(allocator.memory_blocks,"\n")


if __name__ == "__main__":
    main()

