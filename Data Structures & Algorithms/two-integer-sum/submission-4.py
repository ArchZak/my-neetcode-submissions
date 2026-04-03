class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs={}
        for i in range(len(nums)):
            diff = target-nums[i]
            if nums[i] in pairs:
                return [pairs[nums[i]],i]
            else:
                pairs[diff]=i