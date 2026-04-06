class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heapify(self.heap)
        heapq.heappush(self.heap, val)
        return heapq.nlargest(self.k, self.heap)[-1]
