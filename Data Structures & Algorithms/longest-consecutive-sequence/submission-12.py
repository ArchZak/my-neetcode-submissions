class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input: an array of integers
        #output: len of longest consec sequence

        #consec sequence: seq of elements where each element is +1 greater than prev
        #NOT consec in array
        #constraints: array is long, and numbers can be negative

        #sort:
        #sort and then count through the array
        #O(nlogn) time O(1) space if .sort()

        #hash map:
        #hash the entire array, loop through each num in array and increment up
        #O(n^2) time O(n) space 
        #hash the entire array, loop through each num in array, start counting if num doesnt have a num-1, avoid duplicate work
        #O(n) time and space

        #set(array), answer = 0
        #for num in nums:
        #   if num-1 doesnt exist, start counting up
        #   otw skip
        #return answer

        #tdd sake:
        #example test case: [0,1,2,3,4,5,6,8] = 7

        tracker, answer = set(nums), 0
        for num in nums:
            if num-1 not in tracker:
                temp=1
                while num+1 in tracker:
                    temp+=1
                    num+=1
                answer = max(answer, temp)
        
        return answer
        
                