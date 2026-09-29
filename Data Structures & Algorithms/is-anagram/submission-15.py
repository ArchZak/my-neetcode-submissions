class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input: strings s and t
        #output: bool if anagram or not

        #two strings s and t, true if anagram, false otw
        #anagram is same characters, same amount of times, order doesnt matter

        #constraints: 
        #string will only have lowercase characters
        #string length will at least be 1, but will inputs be equal len?

        #test cases:
        # s = "isgfosdgfcosdfghcb" t = "a" output: false
        # s = "onetwothree" t = "onetwothree" output true
        # s = "aasdfg" t = "agfdsa" output: true

        #double for loop
        #just double in and count everything 

        #hash array
        #since 26 letters, array [0]*26 and then for letters in s, add 1, for letters in t, minus 1
        #then check the list after to see if we have any numbers that arent 0

        #hash dict
        #for every letter in s, add it as key to dict and add 1
        #for every letter in t, minus 1

        #init hash map
        #for loop:
        #   to add 1s to the list using s
        #for loop to minus 1s to the list using t
        #checking the values for nums that aint 0

        tracker = {}
        for letter in s:
            tracker[letter] = tracker.get(letter, 0)+1

        for letter in t:
            tracker[letter] = tracker.get(letter, 0)-1

        for key, value in tracker.items():
            if value != 0:
                return False

        return True
            


