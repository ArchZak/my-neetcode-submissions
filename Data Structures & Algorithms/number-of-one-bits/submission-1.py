class Solution:
    def hammingWeight(self, n: int) -> int:
        #input: 32b uint
        #output: the number of 1 bits in the given number

        #loop through the 32 bits and bitwise AND against curr index
        #will evaluate to true if the 1 survive 

        answer = 0 
        for i in range(32):
            if 1 << i & n:
                answer+=1
        return answer