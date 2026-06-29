class StockSpanner:

    def __init__(self):
        self.stack = [] #values are (price,span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))
        return span
        
#the trick for stacks is that if youre gonna pop info, need to track old stuff
#span is the number of days going backward(include today) where stock price is less/equal price today

#next implement:
#so while stack and the price at top of stack is less than curr
#increase the span while iterating, and pop item off
#when exit, push new price with its span on