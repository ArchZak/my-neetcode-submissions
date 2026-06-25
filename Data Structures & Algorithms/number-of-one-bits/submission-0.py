class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        for i in range(32):
            if (1 << i) & n:
                answer+=1
        return answer