class Solution:
    def countBits(self, n: int) -> List[int]:
        #input: uint n
        #output: list of num of 1s for every num in range [0,n]

        answer = [0]*(n+1)
        for i in range(n+1):
            temp = 0
            for j in range(32):
                if (1 << j) & i:
                    temp +=1
            answer[i]=temp
        
        return answer