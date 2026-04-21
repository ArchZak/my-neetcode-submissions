class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #input: array of integers and k for window
        #output: an array of each max in the window

        #iterate through the list one at a time
        #take the max of the window and append it to answer

        answer = []
        i = 0
        while i+k-1 < len(nums):
            answer.append(max(nums[i:i+k]))
            i+=1

        return answer
