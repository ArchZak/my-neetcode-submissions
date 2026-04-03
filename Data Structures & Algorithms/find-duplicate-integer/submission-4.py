class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #input: nums array with n+1 ints, where each int is in [1,n]
        #every int appears exactly once, except for 1 that doesnt(more than 1)
        #output: num that appeared more than once

        #constraints, 1<=n, the length
        #we can modify the array as we go, by turning numbers we've seen negative. 
        #using the curr val-1 for 0 index, and then check if that val is negative or not
        #if negative, return.
        #[1,3,4,2,2] 1
        #[-1,3,4,2,2]

        for num in nums:
            index = abs(num)-1
            if nums[index] < 0:
                return abs(num)
            nums[index]*=-1
        return -1