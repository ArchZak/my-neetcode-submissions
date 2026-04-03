class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #input: two words of only lowercase letters and potentially diff lengths
        #output: an alternating string

        #while i < len of either string
        # add them alternately
        #exit loop and then do + word1 or word2 idk

        i = 0
        answer = ""
        while i < len(word1) and i < len(word2):
            answer+=word1[i] #put word 1 first
            answer+=word2[i] #put word 2 second
            i+=1

        if i < len(word1):
            answer += word1[i:]
        elif i < len(word2):
            answer += word2[i:]
        
        return answer
