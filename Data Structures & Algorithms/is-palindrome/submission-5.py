class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while not s[left].isalnum() and left < right:
                left+=1
            while not s[right].isalnum() and left < right:
                right-=1
            if s[right].lower() == s[left].lower():
                right-=1
                left+=1
            else:
                return False
        
        return True