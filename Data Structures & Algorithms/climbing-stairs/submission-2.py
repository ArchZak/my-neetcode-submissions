class Solution:
    def climbStairs(self, n: int) -> int:
        #just gonna dfs to find problem

        #base case is when we reach 5, add one
        #base case is if over 5, add 0
        tracker = [0]*(n+1)
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if tracker[i] != 0:
                return tracker[i]

            curr_step = dfs(i+1)+dfs(i+2)
            tracker[i] = curr_step
            return curr_step

        return dfs(0)

            