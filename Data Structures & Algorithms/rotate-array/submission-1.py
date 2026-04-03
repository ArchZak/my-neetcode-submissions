class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #input: given int array nums, given k (non-neg: >=0)
        #output: rotated array where array is rotated k times. in place

        #loop through range of k
        #pop and then insert the item at 0

        length = len(nums)
        for i in range(k % length):
            nums.insert(0,nums.pop()) 

        