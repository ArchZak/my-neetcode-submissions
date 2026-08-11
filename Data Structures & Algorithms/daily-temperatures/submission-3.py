class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input: an array of temperatures for ith day
        #output: list where i is number of days after that day before warmer appears

        #need a list of len temp to just be 0s -> [0]*len(temperatures)
        #going to use a monotonic stack to store (temp, index)
        #means we want a stack to have decreasing items to clarify
        #if we want to push on a new val and it's bigger than prev
        #^^start popping values and then do index - index and then place num at index of tup in stac
        #we'll enforce this until we're done looping through temps

        #brute force wouldve just been to double for loop

        answer = [0]*len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                curr_temp, curr_index = stack.pop()
                answer[curr_index] = index-curr_index
            else:
                stack.append((temp, index))


        return answer