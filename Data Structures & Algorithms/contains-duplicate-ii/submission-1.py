class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #given int array nums, and an int k
        #output: true if 2 distinct i and j such that the values are equal and abs(i-j)<=k. false otw

        #want to solve this problem in one pass
        #need to loop through the whole arrya, so no ending early
        #have a set that tracks the keys we come across
        #if we have a key thats in the set, run it through the test, return true if passes, cont if otw
        #return false if you get through the whole array

        tracker = {}

        for i, num in enumerate(nums):
            if num not in tracker:
                tracker[num] = i
            else:
                if abs(tracker[num]-i) <= k:
                    return True
                else:
                    tracker[num] = i

        return False
        
