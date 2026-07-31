# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #input: the range within a number is the target
        #output: the target that the API chose

        #-1 if too high, 1 if too low, 0 if spot on

        left, right = 1, n
        while left <= right:
            mid = (left+right)//2
            if guess(mid) < 0: #so if too high
                right = mid-1
            elif guess(mid) > 0: #so if too low
                left = mid+1
            else:
                return mid