class MinStack:
    def __init__(self):
        self.stack=[]   
        self.min_stack=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value,self.min_stack[-1]))
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

#Approach: The code implements a MinStack class that supports push, pop, top, and retrieving the minimum element in constant time. It uses two stacks: one for storing the actual values and another for keeping track of the minimum values. When a new value is pushed onto the stack, it is compared with the current minimum (the top of the min_stack) and the smaller of the two is pushed onto the min_stack. When popping, both stacks are popped to maintain synchronization.

#time complexity: O(1) for all operations (push, pop, top, getMin) since we are using stacks and each operation takes constant time.

#space complexity: O(n), where n is the number of elements in the stack. This is because we are using two stacks to store the values and the minimums, which can grow linearly with the number of elements pushed onto the stack.