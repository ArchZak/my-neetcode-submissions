class Solution:
    def reverseBits(self, n: int) -> int:
        #input: 32b uint 
        #output: the same int but reversed

        #when reversing, bit at i goes to 31-i

        answer = 0
        for i in range(32):
            if (n >> i) & 1:
                answer |= 1 << (31-i)
        
        return answer