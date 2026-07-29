class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input: an array of integers 
        #output: the len of longest consecutive sequence of elements that can be formed

        #consecutive sequence meaning that each element is 1 bigger than prev, no consec in array
        #we want to find a num where num-1 of that doesnt exist in the given sequence
        #hash the entire array and then loop through it for a num without num-1
        #once we find it, start a while loop to get our inc, then count that for max

        tracker = set(nums)
        answer = 0
        for num in tracker:
            counter = 0
            if num-1 not in tracker:
                while num+counter in tracker:
                    counter+=1
            answer = max(answer, counter)

        return answer
