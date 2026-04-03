class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # inputs: int nums
        # return: output array where output[i] is product of all elements except nums[i]

        # prefix postfix approach
        # prefix loops forward, so start prefix as 1
        # prefix will multiply output array, then scale it up using nums

        # postfix loops backwards, we'll start it on 1
        # postfix loops backwards, so start postfix as 1
        # postfix will multiply output array, then scale up using nums

        output = [1]*len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            output[i]*=prefix
            prefix*=nums[i]

        for i in range(len(nums)-1,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]

        return output