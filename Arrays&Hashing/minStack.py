# Min Stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) #get minimum of val or most recent element in minStack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# OR BETTER

class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.min)==0): #if min stack is empty, append val
            self.min.append(val)
        else:
            if(self.min[-1]>=val): #if recent element in min stack is greater than val, append val
                self.min.append(val)
                

    def pop(self) -> None:
        if(self.stack[-1]==self.min[-1]): #if the recent element of stack and min are the same, delete recent min and stack elements
            del self.min[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()