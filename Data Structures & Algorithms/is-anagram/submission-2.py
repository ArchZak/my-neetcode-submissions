class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #    s_string = sorted([letter for letter in s])
    #    t_string = sorted([letter for letter in t])
    #    return s_string == t_string
        return sorted([letter for letter in s]) == sorted([letter for letter in t])