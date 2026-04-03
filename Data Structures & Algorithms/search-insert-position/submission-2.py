class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            median = (right+left)//2
            if nums[median] < target:
                left = median+1
            elif nums[median] > target:
                right = median-1
            else:
                return median
        return (right+left)//2 + 1