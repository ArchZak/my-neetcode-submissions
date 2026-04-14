class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #loop through og given string
        #compare each letter to curr letter of sub
        #if match, move forward in sub comparing

        #if you end early then just return true
        #otw check index and return

        i = 0
        for letter in t:
            if i < len(s) and s[i] == letter:
                i+=1
            elif i >= len(s)-1:
                return True

        return i == len(s)