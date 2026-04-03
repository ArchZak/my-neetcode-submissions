class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            median = int((right+left) / 2)
            print(median)
            if nums[median] < target:
                left = median+1
            elif nums[median] > target:
                right = median-1
            else:
                return median
        return -1
    