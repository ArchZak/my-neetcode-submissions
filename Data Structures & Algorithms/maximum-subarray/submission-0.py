class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = sum(nums)

        for i in range(len(nums)):
            j=0
            while j+i < len(nums):
                answer = max(answer, sum(nums[j:j+i+1]))
                j+=1
        
        return answer