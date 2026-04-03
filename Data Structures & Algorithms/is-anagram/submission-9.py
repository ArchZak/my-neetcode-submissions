class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two strings s and t
        #true if anagrams, false if not
        #same chars
        #only contain lower case english letters
        #no edgecases

        #[0]*26
        #add 1 in s, subtract 1 in t
        #if entire array = 0, then it's true
        #if the lens are diff, cancel immeidately

        #checker for lens
        #one loop for s to increment places
        #one loop for t to decrement places
        #last loop to check if all places are 0

        if (len(s) != len(t)): #o(n)
            return False
        
        array_hash=[0]*26 #26 letters in alphabet, ord('s[i]')-ord('a')

        for letter_s in s:
            array_hash[ord(letter_s)-ord('a')]+=1
        
        for letter_t in t:
            array_hash[ord(letter_t)-ord('a')]-=1
        
        for num in array_hash:
            if num != 0:
                return False

        return True


        