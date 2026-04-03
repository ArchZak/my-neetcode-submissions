class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #input: numbers in asec order, int target
        #output: 1-indexed [index1,index2] where theyre not equal, and index1<index2, and add up to target
        #SPECIFICALLY RETURN THE 1INDEXED INDICES
        #O(1) SPACE ONLY

        #two pointers, one at left, one at right
        #while l < r, if l+r<k -> increment l, if l+r>k, decrement r, otw return 1-indexes
        #return [l=1,len-r+1]

        left, right = 0, len(numbers)-1

        while left < right:
            if numbers[left]+numbers[right] == target:
                return [left+1,right+1] #base case, indices found
            elif numbers[left]+numbers[right] < target:
                left+=1
            elif numbers[left]+numbers[right] > target:
                right-=1
            
