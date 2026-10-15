class Solution:
    def rob(self, nums: List[int]) -> int:
        #input: #int array nums where value is amount of money index has
        #output: max money you can rob without alerting police

        #general
        
        #house is in straight line, neighbor is i-1 and i+1 to i
        #wanna rob house but cant rob adjacent houses
        #so decision tree, either rob house or dont
        #if you do, go up 2, if you dont, go up 1

        #subproblem: you just go every other at that house, kinda greedy
        #starting at the index, if you rob every other that's the cash you'd make

        #constraints + edge cases
        #will have at least one house
        #cash in house is nonnegative

        #tests + examples
        #nums = [1,1,3,3]
        #answer is 4 bc 1 + 3
        #0 2 , 1 3 , 0 4

        #nums = [2,9,8,3,6]
        #answer is 16 bc 0 2 4

        #nums = [2,9,8,8,8,3,10] 2+8+8+10=28 9+8+3+10=30

        #english
        #subproblem: you just go every other at that house, greedy
        #starting at the index in cache, if you rob other houses after that most cash youd make
        #dfs through array
        #base case: if at end of array just return 0
        #recursive case: rob curr block then jump 2, skip curr block and jump 1

        #pseudo
        #cache = [-1]*len(nums)
        # def dfs(i):
        #   if i is out of bounds return 0
        #   if we've been at this index before just take the cache we'd make
        #   cache[i] = max(dfs(i+1), dfs(i+2))
        #   return cache[i]

        cache = [-1]*len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(dfs(i+1),dfs(i+2)+nums[i])
            return cache[i]

        dfs(0)
        return max(cache)


