class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input: given list of strings
        #output: sort strings into sublists of anagrams

        #general
        #given array of strings, group anagrams together in sublists, in any order
        #anagram is when strings have exact same letters, regardless of order

        #constaints+edge cases
        #will have at least one string
        #strings can be empty tho
        #only lowercase letters -> so easy ord if we wanted

        #testing + examples
        #string full of words
        #string wtih one word/empty sentence

        # [act, cat] [pots, tops, stop] [hat]

        # [""]

        #english: key value pair (hash)
        #going to loop through words in strs
        #need to make a key out of the word, [0]*26, tuple, key into dict where value is list
        #return dict values

        #pseudo
        #tracker = {} #tuple: [strings, here]
        #for word in words:
        #   for letter in word turn it into list
        #   turn it into tuple then make key value pair
        #return tracker.values()

        hashmap = {}
        for word in strs:
            anagram = [0]*26
            for letter in word:
                anagram[ord(letter)-ord('a')]+=1
            key = tuple(anagram)
            # hashmap[key] = hashmap.get(key, []).append(word)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        return [list(x) for x in hashmap.values()]




