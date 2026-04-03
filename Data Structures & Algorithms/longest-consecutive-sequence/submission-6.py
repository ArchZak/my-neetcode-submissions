class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        answer=0

        for num in nums_set:
            if num-1 not in nums_set: #this rs counter
                counter=1
                while counter+num in nums_set: #will only go if exists tho, weird indent
                    counter+=1
                answer = max(answer,counter)

        return answer