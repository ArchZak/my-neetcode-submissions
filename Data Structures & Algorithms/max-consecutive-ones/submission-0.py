class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer, temp = 0, 0
        

        for i in range(len(nums)):
            if nums[i] == 1:
                temp+=1
                answer = max(answer,temp)
            else:
                temp = 0

        return answer