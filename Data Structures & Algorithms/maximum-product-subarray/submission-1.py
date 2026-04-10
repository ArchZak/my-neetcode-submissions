class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import math
        answer = nums[0]

        for i in range(len(nums)):
            j=0
            while j+i+1 < len(nums)+1:
                # temp = 1
                # for num in nums[j:j+i+1]:
                #     temp*=num
                answer = max(answer,math.prod(nums[j:j+i+1]))
                j+=1

        return answer

        #brute force approach
        #computem product of each subarray and take the max