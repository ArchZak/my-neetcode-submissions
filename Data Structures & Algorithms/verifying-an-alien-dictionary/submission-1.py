class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #input: a list of words, the string that makes up the dictionary for alien
        #output: whether or not the given words are in order or not

        #loop through two words at a time
        #loop through the two words until you find a diff
        #grab the first diff, check their order in the dict, if it's fine, continue on to next two words

        tracker = {order[num]: num for num in range(len(order))}

        for i in range(1,len(words)):
            for j in range(len(words[i-1])): #loop through the second word
                if j == len(words[i]):
                    return False
                elif words[i][j] != words[i-1][j]:
                    if tracker[words[i-1][j]] > tracker[words[i][j]]:
                        return False
                    break

        return True