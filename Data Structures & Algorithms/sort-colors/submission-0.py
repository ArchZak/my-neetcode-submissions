class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tracker = {0:0,1:0,2:0}
        
        for num in nums:
            tracker[num]+=1
        
        j=0
        for key, val in tracker.items():
            i=0
            while i < val:
                nums[j] = key
                i+=1
                j+=1