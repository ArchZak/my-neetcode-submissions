class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        given array of ints with n+1 ints
        each int in ^ is in range [1,n] inclusive

        there is exactly one repeated int, every other int shows up at most once
        return the repeated int

        n is at least 1
        nums length is n+1
        all ints are positive and less than n
        so the repeat will just be > 1 time

        approaches:
        
        negative indexing:
            we loop through the array
            we use the val to negate the index
            if its already negated, then we found our dupe

        literal:
            for each num in nums
                check the index, if negative return num
                if not negative than make it negative

        1,-2,-3,-4,4
        """

        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            nums[abs(num)]=-nums[abs(num)]

