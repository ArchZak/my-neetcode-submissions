class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #input: arr of ints + num of ints to return + target int
        #output: list of size k of closest ints

        #two pointer solve to find smallest window
        #while right-left > k, gonna shrink the pointers down
        #if a-x < b-x, then gonna shrink right
        #otw we increase left

        left, right = 0, len(arr)-1
        while right-left+1 > k:
            if abs(arr[left]-x) <= abs(arr[right]-x) and arr[left] < arr[right]:
                right-=1
            else:
                left+=1
        return arr[left:left+k]
