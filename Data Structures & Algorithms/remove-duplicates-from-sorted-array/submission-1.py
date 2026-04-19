class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #input: int array of increasingh order
        #output: num array where we delete duplicates in place and number of unique elements

        #dont care about elements outside first k positions of array
        #to be accepted, first k elements need to contain unique elements

        #fast and slow pointer approach
        #so have left pointer be the curr value we're checking for dupes
        #have a right pointer check for unique value, exit whenever found
        #exit loop and just return l whenever through whole array

        left, right = 0, 0

        while right < len(nums):
            nums[left] = nums[right]
            while right < len(nums) and nums[left] == nums[right]:
                right+=1
            left+=1

        return left