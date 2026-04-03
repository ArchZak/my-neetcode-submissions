class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracking = set()
        left, answer = 0, 0

        for right in range(len(s)):
            while s[right] in tracking:
                tracking.remove(s[left])
                left+=1
            tracking.add(s[right])
            answer = max(right-left+1,answer)
        
        return answer