class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input: array of ints where i is temp of that day
        #output: array of results where i is num of days after i before warmer day happens

        #going to use a stack where its (value, index)
        #iterate through array and add values to the stack
        #when we come across a value that isnt in decreasing order
        #we start popping until top of stack isnt less than curr element
        #while popping, compute diff between indices are store it in the pos of the index

        stack, results = [], [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            if stack and stack[-1][0] < temp:
                while stack and temp > stack[-1][0]:
                    curr = stack.pop() #value, index
                    results[curr[1]] = index-curr[1]
                
            stack.append((temp, index))

        return results