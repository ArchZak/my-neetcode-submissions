class Solution:
    def scoreOfString(self, s: str) -> int:
        #input: a string s
        #output: the score of the string

        #score of string is defined as sum of abs diff between ASCII values of adjacent characters
        #loop through stirng and just add abs diff of i and i-1 to answer

        answer = 0
        for i in range(1,len(s)):
            answer+=abs(ord(s[i])-ord(s[i-1]))

        return answer