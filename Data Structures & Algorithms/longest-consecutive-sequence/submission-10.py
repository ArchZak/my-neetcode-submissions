class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums=set(nums)
        counter, answer = 0,0

        for num in hash_nums:
            if num + counter in hash_nums:
                while num + counter in hash_nums:
                    counter+=1
                answer = max(answer,counter)
                counter=0
        
        return max(answer,counter)