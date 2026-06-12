class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #input: array of ints and a target int
        #output: len of the smallest array whose values >= target

        #subarray = contig, nonempty array,if no sub array, return 0

        #sliding window approach
        #start with size 1 and increment up until len of array

        for i in range(1,len(nums)):
            for j in range(len(nums)-i+1):
                if sum(nums[j:j+i]) >= target:
                    return len(nums[j:j+i])

        return len(nums) if sum(nums) >= target else 0