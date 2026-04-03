class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict={}

        for word in strs:
            hash_arr=[0]*26
            for letter in word:
                hash_arr[ord(letter)-ord('a')]+=1
            if tuple(hash_arr) not in hash_dict:
                hash_dict[tuple(hash_arr)] = [word]
            else:
                hash_dict[tuple(hash_arr)].append(word)

        return list(hash_dict.values())
