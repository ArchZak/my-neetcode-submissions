class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict={}

        for word in strs: #o(n) where n is len of array
            hash_arr=[0]*26
            for letter in word: #o(m) where m is len of word
                hash_arr[ord(letter)-ord('a')]+=1

            hash_tuple=tuple(hash_arr)

            if hash_tuple in answer_dict:
                answer_dict[hash_tuple].append(word)
            else:
                answer_dict[hash_tuple]=[word]

        return list(answer_dict.values())
            
            