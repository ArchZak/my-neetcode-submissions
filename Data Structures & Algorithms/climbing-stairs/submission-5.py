class Solution:
    def climbStairs(self, n: int) -> int:
        #input: int to rep number of steps to reach top
        #output: number of distinct ways to reach the top of the stairs

        #general
        #you can climb either 1 or 2 steps at a time (backtracking, dfs)

        #constraints + edge cases
        #will have at least 1 step
        #need to land on actual step, cant go over and count it
        #want permutations not combos

        #tests + examples
        
        #n = 4

        #0 1 2 3 4 3 5
        #have to do a lot of repeated work, track previous answers in array
        #the index refers to how many ways there are to get to n

        #english
        #going to dfs through decision tree
        #base case is check cache, check if == n, check if > n. return cache, 1, 0 respectively
        #recursive case is kick off at +1 and +2, save answer for that and put it in cache and return that

        #pseudo
        #tracker = [0]*n
        # def dfs(curr):
        #base case
        #   if == n return 1, if > n return 0, if cache has value in it then return that
        #recursive case
        #   cache[curr] = dfs(curr+1)+dfs(curr+2) and return cache
        
        tracker = {}
        def dfs(curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            if tracker.get(curr):
                return tracker[curr]

            tracker[curr] = dfs(curr+1)+dfs(curr+2)
            return tracker[curr]

        return dfs(0)




