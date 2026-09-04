class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #input: array of integers
        #output: all values, no dupes as array of arrays. values can dupe jsut no indices

        #find all triplets where indepedent indices == 0
        #so i, j, k are distinct and values in array add up to 0

        #constraints:
        #array is at least 3 long
        #values can be negative or positive

        #triple for loop
        #just three for loops check every combo that way
        #O(n^3) time and O(n) space

        #two pointer + for loop
        #we have a for loop and each instance kicks off a two pointer where l<r so l + r + m
        #handle dupes by sorting inputs and adding to set which we will return as list
        #O(n^2) time and O(n) space

        #does array come sorted?

        #answer, tracker = list, set
        #for num in nums:
        #   left, right = 0, len(nums)-1
        #   while left < right:
        #       if too big, move right down
        #       if too small, move left up
        #       if equals 0, then
        #           make sure to not have right or left be on mid indice
        #           sort inputs into tuple, check tracker, if not in, add to tracker and array :D

        nums.sort()
        answer, tracker = [], set()
        for mid, num in enumerate(nums):
            left, right = 0, len(nums)-1
            while left < right:
                if left == mid:
                    left+=1
                    continue
                if right == mid:
                    right-=1
                    continue
                curr = nums[left]+nums[right]+nums[mid]
                if curr < 0:
                    left+=1
                elif curr > 0:
                    right-=1
                else:
                    triplet = tuple(sorted([nums[left],nums[mid],nums[right]]))
                    if triplet not in tracker:
                        tracker.add(triplet)
                        answer.append(list(triplet))
                    left+=1
                    right-=1
        
        return answer