class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input: array of ints
        #output: another array of ints

        #array of ints where each val is temp of that day
        #return array where index is number of days after where warmer apears
        #if no day then just put 0

        #stack
        

        answer, stack = [0]*len(temperatures), [] #[temp, index]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, j = stack.pop()
                answer[j] = i-j
            stack.append([temp, i])

        return answer
        