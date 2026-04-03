class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #input: array of strings
        #output: longest common prefix of ALL strings, return "" if none

        #use first word as a reference
        #loop through other words in the array
        #if all of them have the same common letter, then append to answer
        #otw return

        answer = ""

        for i in range(len(strs[0])): #O(m+n) where m is len of string and n is array len
            tracker = 0
            for word in strs:
                if len(word) > i and strs[0][i] == word[i]:
                    tracker+=1
            
            if tracker == len(strs):
                answer+=strs[0][i]
            else:
                return answer
        
        return answer