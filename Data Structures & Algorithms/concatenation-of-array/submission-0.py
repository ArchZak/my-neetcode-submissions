class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #input: int array nums of length n
        #create array of len 2n where ans[i] == nums[i]
        #and ans[i+n] == nums[i]
        #output: ans as concat of two nums arrays

        return nums+nums