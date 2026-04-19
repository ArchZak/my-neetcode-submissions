class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #input: int array of increasingh order
        #output: num array where we delete duplicates in place and number of unique elements

        #dont care about elements outside first k positions of array
        #to be accepted, first k elements need to contain unique elements

        #have a set to track unique numbers
        #if we encounter a num that's in the set, change its value so it can be sorted later and forced to end
        #return len of set and sort array before returning

        tracker = set()

        for i, num in enumerate(nums):
            if num in tracker:
                nums[i] = 101
            else:
                tracker.add(num)

        nums.sort()
        return len(tracker)
