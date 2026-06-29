class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 0
        self.stack.append(price)
        temp = self.stack.copy()
        while temp and temp.pop() <= price:
            span+=1
        return span
        
#span of the stocks price in 1 day is max num of consec days going back
#that the stock price today is less/equal to price of today

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)