class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = [[]]
        answer = 0
        for num in nums:
            subset+=[curr + [num] for curr in subset]
        
        for sub in subset:
            temp = 0
            for num in sub:
                temp^=num
            answer+=temp

        return answer