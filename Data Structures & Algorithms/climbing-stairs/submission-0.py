class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(n):
            if memo[n] is not None:
                return memo[n]
            if n == 0 or n == 1:
                memo[n] = 1
                return memo[n]
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]

        memo = [None]*(n+1)
        return dp(n)