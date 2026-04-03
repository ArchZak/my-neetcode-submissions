class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        answer=0

        for num in nums_set:
            if num-1 not in nums_set:
                counter=1
                while counter+num in nums_set:
                    counter+=1
                answer = max(answer,counter)

        return answer