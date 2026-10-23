class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s and t are lowercase english letters
        same len same amount of characters to make anagrams
        return true if anagram return false otw

        hash array
            gonna use array [0]*26
            gonna loop through letters and compare

        hash set
            compare letters are keys

        loop through first string and inc
        loop through second string and dec
        compare if any 0s left
        """

        hasharray = [0]*26

        for letter in s:
            hasharray[ord(letter)-ord('a')]+=1

        for letter in t:
            hasharray[ord(letter)-ord('a')]-=1

        for num in hasharray:
            if num != 0:
                return False

        return True

