class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            counter = [0]*26
            for letter in word:
                counter[ord(letter)-ord('a')]+=1

            counter = tuple(counter)
            
            if counter not in hash_map:
                hash_map[counter]=[word]
            else:
                hash_map[counter].append(word)

        return list(hash_map.values())