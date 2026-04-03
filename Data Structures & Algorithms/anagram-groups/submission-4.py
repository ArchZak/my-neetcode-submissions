class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # need to loop through array
        # another loop to loop through letters
        # hash map with tuple keys, so we'll do [0]*26
        # values will be arrays of the words that fit into anagrams
        # return list(dict.values())

        # n is strs len
        # m is word len
        # O(m*n) -> time

        # n
        # 26 array + 26 tuple
        # n -> space

        hash_map = {}

        for word in strs:
            hash_array = [0]*26 #26 letters in the alphabet

            for letter in word:
                hash_array[ord(letter)-ord('a')]+=1 #should be in 0-25 range
            hash_tuple = tuple(hash_array) #keys need to be immutable

            if hash_tuple in hash_map:
                hash_map[hash_tuple].append(word) #if tuple exists, append word
            else:
                hash_map[hash_tuple] = [word] #if not yet, init with new word

        return list(hash_map.values())