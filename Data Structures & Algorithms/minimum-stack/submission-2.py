class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val,self.getMin()))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
#design stack with normal ops + getMin
#each needs to run in O(1) time

#minstack is init
#push puts val onto stack (the top)
#pop removes item from stack (the top)
#top is a peaksie
#getMin is smallest minimum element in the stack

#2 stacks, one for your normal day to day operations
#another for tracking the minimum value
#wont get null ops