class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #input: array of nums with unsorted int array
        #output: smallest positive int not present in nums

        #need to use O(n) time with O(1) space

        #prob need to init answer to 0

        #use for loop to get through the array
        #check if curr val is positive and +1 than curr answer
        #if it is, then make it the new value
        #sentinel variable in here for while loop
        
        #multiple passes may be needed
        #while loop with sentinel to indicate we didnt increment the value?

        #eventually just return answer+1

        answer = 0
        sentinel = True

        while sentinel:
            changes = 0
            for num in nums:
                if num == answer+1:
                    answer+=1
                    changes+=1

            if changes == 0:
                sentinel = False
            

        return answer+1

