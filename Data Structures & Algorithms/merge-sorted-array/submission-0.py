class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #input: given 2 int arrays both in ascending order along with m and n
        #m is num of valid inputs in nums1 and n is len of nums2
        #basically replace the m->m+n in nums1 with nums2
        #output: nums1 so do it in place, also want array sorted

        for i in range(m,m+n,1):
            nums1[i] = nums2[i-m]
        
        nums1.sort()


        