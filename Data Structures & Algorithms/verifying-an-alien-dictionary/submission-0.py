class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #input: words, and order
        #output: true iff words are sorted lexicographically in alien language

        #order: is alphabet with permutation of all 26 lowercase letters in english, as single string
        #words: is array of strings in the alien language

        #want to confirm if the words array itself is sorted

        #need to search through the characters to find the first different once
        #need to search for first occurence of failure or success
        #going to compare i against i-1
        #if we find a letter in i and i-1 that arent equal, check their ordering, if it's good, move on to another pair
        #if word2 ends before word1, then auto fail as well

        tracker = { letter: index for index, letter in enumerate(order)}
        
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]

            for j in range(len(word1)):
                if j == len(word2): #word1 should be shorter, so exit if not
                    return False
                elif word1[j] != word2[j]:
                    if tracker[word1[j]] > tracker[word2[j]]:
                        return False
                    break
        
        return True


