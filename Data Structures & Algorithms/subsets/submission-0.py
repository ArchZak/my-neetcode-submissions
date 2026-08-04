class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset= [[]]
        for num in nums:
            subset+=[curr+[num] for curr in subset]
        return subset