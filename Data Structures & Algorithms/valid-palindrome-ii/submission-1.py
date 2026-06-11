class Solution:
    def validPalindrome(self, s: str) -> bool:
        #input: string s
        #output: if string s is a palindrome or not 

        #brute force problem
        #delete a character and compare
        if s[::-1] == s:
            return True

        for i in range(len(s)-1):
            temp = s[:i] + s[i+1:]
            if temp[::-1] == temp:
                return True

        return False