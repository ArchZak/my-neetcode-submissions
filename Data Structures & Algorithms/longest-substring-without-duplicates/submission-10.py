class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: given string s
        #output: len of longest substring without dupe characters

        #general
        #substring is contig sequence of characters within a string

        #constraints + edge cases
        #string could be len 0
        #capital characters included, so theyre diff, dont filter or change inputs, any ascii char

        #solving: sliding window approach
        #we move left pointer up when we find a dupe
        #we move right pointer up otw

        #tests + examples
        #pwwkew

        hashset = set()
        left, right, answer = 0, 0, 0

        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                right+=1
            else:
                hashset.discard(s[left])
                left+=1
            answer = max(answer, right-left)
            
        return answer