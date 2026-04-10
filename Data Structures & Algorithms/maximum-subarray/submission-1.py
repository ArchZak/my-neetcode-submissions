class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = sum(nums)

        for i in range(len(nums)):
            j=0
            while j+i < len(nums):
                answer = max(answer, sum(nums[j:j+i+1]))
                j+=1
        
        return answer

        #brute force approach
        #growing sliding window, start with 1 len and slide it 1 at a time
        #grow window by size 1 until it's the size of actually array