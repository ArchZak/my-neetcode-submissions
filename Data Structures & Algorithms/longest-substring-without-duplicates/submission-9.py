class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: string with characters
        #output: find length of longest substring without dupes

        #substring is a contig sequence of characters in the string
        #going to for loop through string to start at letter
        #then gonna have while loop tick up and track unique letters

        answer = 0
        for index, letter in enumerate(s):
            tracker = set()
            counter = 0
            while counter+index < len(s) and s[counter+index] not in tracker:
                tracker.add(s[counter+index])
                counter+=1
            answer = max(answer, counter)

        return answer