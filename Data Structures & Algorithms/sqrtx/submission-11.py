class Solution:
    def mySqrt(self, x: int) -> int:
        #input: a non negative integer x
        #output: return the floored square root

        #loop through numbers up to x
        #the first time we get a number higher than x, return that -1

        if x < 2:
            return x

        for i in range(x+1):
            if i*i > x:
                return i-1