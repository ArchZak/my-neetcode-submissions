class Solution:
    def maxScore(self, s: str) -> int:
        #input: string of 1s and 0s
        #output: max score after spliting the string

        #score = number of 0s on elft + number of 1s on right

        #split the string each time, count 0s, count 1s

        answer = 0
        temp = 0

        for i in range(1,len(s)):
            for num1 in s[:i]:
                if num1 == '0':
                    temp+=1
            for num2 in s[i:]:
                if num2 == '1':
                    temp+=1

            answer = max(answer, temp)
            temp = 0
    
        return answer