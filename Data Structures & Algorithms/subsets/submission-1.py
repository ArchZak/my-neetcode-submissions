class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for num in nums:
            subset+=[sub + [num] for sub in subset]
        return subset