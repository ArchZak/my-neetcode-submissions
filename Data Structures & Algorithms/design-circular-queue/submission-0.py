class MyCircularQueue:

    def __init__(self, k: int):
        # init obj with size k to be queue
        self.length = k
        self.queue = []
        

    def enQueue(self, value: int) -> bool:
        # add item to queue, true if successful
        if self.isFull():
            return False
        
        self.queue.insert(0, value)
        return True
        

    def deQueue(self) -> bool:
        # delete elment from circular queue, true if successful
        if self.isEmpty():
            return False
        
        self.queue.pop()
        return True


    def Front(self) -> int:
        # get front item of queue or -1 if empty
        return -1 if self.isEmpty() else self.queue[-1]

    def Rear(self) -> int:
        # get last item in queue or -1 if empty
        return -1 if self.isEmpty() else self.queue[0]

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.length



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()