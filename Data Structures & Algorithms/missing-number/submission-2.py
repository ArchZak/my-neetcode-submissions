class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #input: a list of ints where it has n ints ranging 0,n without dupes
        #output: return the single num in the range that is missing

        #XOR will return 0 if the numbers are identical
        #so loop through nums, return the first occur of not 0
        #needs sorted array

        nums.sort()

        for i in range(len(nums)):
            if i ^ nums[i]:
                return nums[i]-1

        return nums[i]+1