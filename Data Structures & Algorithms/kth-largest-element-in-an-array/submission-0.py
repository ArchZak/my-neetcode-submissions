class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #input: unsorted array of ints, an int k
        #output: return the kth largest element in sorted order

        #cant just sort the array

        #can negate the whole thing with a list comp -> option
        #heap data structure
        #heapify, it natively creates a minheap O(n)
        #heapq, to look up x number of biggest values, or just pop em off log(k)

        #k wont be out of bounds
        #nums can be anything

        heapq.heapify(nums)
        largest_nums = heapq.nlargest(k, nums)
        return largest_nums[-1]

