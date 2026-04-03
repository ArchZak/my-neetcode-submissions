class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracking = set()
        l = 0
        answer = 0

        for r in range(len(s)):
            if s[r] in tracking:
                while l < r and s[r] in tracking:
                    tracking.remove(s[l])
                    l+=1
                tracking.add(s[r])
            else:
                tracking.add(s[r])
            answer = max(answer,r-l+1)
        
        return answer

        
        
        

        

        