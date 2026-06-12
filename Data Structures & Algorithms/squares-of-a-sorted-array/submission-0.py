class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #input: sorted array of integers
        #output: sorted array of squared ints

        return sorted([num**2 for num in nums])