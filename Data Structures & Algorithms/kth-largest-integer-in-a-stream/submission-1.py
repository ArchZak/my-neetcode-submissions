class KthLargest:
    #inputs: given nums, and int k
    #where k is the kth largest integer
    #output: do add op and return kth largest integer

    #constraints: at least k ints in stream when you search

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        import heapq
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return (heapq.nlargest(self.k, self.heap))[-1]
        
