class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #input: unsorted array of ints, int k
        #output: return kth largest int from sorted version of array

        #given unsorted array of ints, and int k
        #need to return kth largest element from the sorted version of thearray

        #cant sort the array

        #constraint:
        #k will be in range of array len
        #values can be negative or positive

        #heap:
        #turn the given array into a max heap, and then pop off k values until we get the value we want
        #python has heapify but that's a min heap by default, so we need to negate values upon append

        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range(k):
            value = heapq.heappop(nums)

        return -value