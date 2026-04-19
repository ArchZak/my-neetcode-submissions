class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #input: int of arrays with n+1 ints and each num is in range 1,n]
        #^^n+1 meaning there is 1 dupe number
        #output: int that shows up more than once

        #loop through array one time
        #to track which numbers seen, turn the index that num would be negative
        #if we encounter a negative num, we'll know we came across that number and can return

        for num in nums:
            i = abs(num)-1
            if nums[i] < 0:
                return abs(num)
            nums[i]*=-1