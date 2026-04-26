class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #input: array of ints nums with n + 1 ints, and each int is in range [1,n]
        #output: return the int that appears more than once

        #only one int shows up more than once

        #loop through the array
        #since each num wont exceed the bounds, we can set whatever to be negative and check

        for num in nums:
            if nums[abs(num)] < 0: #so if alr negative
                return abs(num)
            nums[abs(num)]*=-1