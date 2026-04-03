class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counters = [0]*26
        for i in range(len(s)):
            counters[ord(s[i])-ord('a')] +=1
            counters[ord(t[i])-ord('a')] -=1
        
        for counter in counters:
            if counter != 0:
                return False
        
        return True