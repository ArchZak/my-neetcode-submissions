class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input: nums array
        #output: nums array product of all except self

        #expand array on each side with a 1
        #do a prefix where you multiply the 1 and then scale it up after multiplying
        #do a postfix where you loop backwards, doing the same thing

        answer = [1]*len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            answer[i]*=prefix
            prefix*=nums[i]

        for i in range(len(nums)-1, -1, -1):
            answer[i]*=postfix
            postfix*=nums[i]

        return answer


