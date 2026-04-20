class Solution:
    def myPow(self, x: float, n: int) -> float:
        #loop abs n times 
        #multiply given x by itself 
        #if negative, return 1/x otw just return x

        answer = 1

        for i in range(abs(n)):
            answer*=x

        if n < 0:
            return 1/answer
        else:
            return answer