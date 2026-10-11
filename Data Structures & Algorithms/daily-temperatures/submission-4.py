class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input: array of temps
        #output: array of when a warmer day happens

        #array of integers where each int is temp on that day of index
        #return array of ints where each val is number of days after curr day where a warmer one happens
        #if no such thing than set value to 0

        #constraints:
        #array will have at least 1 val
        #values will be positive

        #stack:
        #need to use stack with [temp,index] to track values
        #we will push items onto stack when curr temp is smaller than top
        #when we wanna add a new item that's bigger, we pop and then sub indexes into array

        #answer = [0]*len temp, stack = []
        #for each temp, index
        #if stack and temp > stack[-1][0]
        #   while temp > stack[-1] pop top off and update answer
        #else: add onto stack

        answer, stack = [0]*len(temperatures), []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, j = stack.pop()
                answer[j] = i-j
            else:
                stack.append([temp, i])

        return answer

