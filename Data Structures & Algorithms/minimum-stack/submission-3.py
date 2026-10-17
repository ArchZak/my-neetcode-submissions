class MinStack:

    def __init__(self):
        #init normal stack and min value stack
        self.stack, self.min_stack = [], []
        

    def push(self, val: int) -> None:
        #we push value onto stack and check curr val for new min or keep old
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
        

    def pop(self) -> None:
        #we pop value from top of stack and also pop from min value stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        #just show the top
        return self.stack[-1]

    def getMin(self) -> int:
        #just show the top of min
        return self.min_stack[-1]

        
#general 
#minstack to init the class
#push to add items onto stack
#pop item from top of stack
#look at item on top of stack
#get min element in the stack, so smallest value at the time of poppin

#every op needs to run in constant time

#constraints + edge cases
#pop, top, getMin will only be called on nonempty stack

#testing + examples
#stack = [1,2]
#min_stack = [1,1]

#english + pseudo
