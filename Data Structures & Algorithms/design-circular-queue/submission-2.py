class MyCircularQueue:
    def __init__(self, k: int):
        self.length = k
        self.curr_length = 0
        self.tail = None
        self.head = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.curr_length+=1

        if self.curr_length == 1:
            self.tail = self.head = Node(value, None, None)
            
            return True

        self.head.prev = Node(value, self.head, None)
        self.head = self.head.prev
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.curr_length-=1

        if self.isEmpty():
            self.tail = self.head = None
            return True

        self.tail = self.tail.prev
        self.tail.next = None
        return True

    def Front(self) -> int:
        return self.tail.val if self.tail else -1

    def Rear(self) -> int:
        return self.head.val if self.head else -1

    def isEmpty(self) -> bool:
        return self.curr_length == 0

    def isFull(self) -> bool:
        return self.curr_length == self.length

class Node:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()