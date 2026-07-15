class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #input: string of only uppercase chars, int k
        #output: number of repeating chars after up to most k replacements

        #have a for loop to track unique characters
        #going to have a for loop that starts at letter
        #have a while loop to increment through
        #during the while loop, if not curr letter, decrement replaces

        answer = 0
        tracker = set(s)
        for curr in tracker:
            for index, letter in enumerate(s):
                counter, replaces = 0, k
                while index+counter<len(s) and (s[index+counter] == curr or replaces > 0):
                    if s[index+counter] != curr:
                        replaces-=1
                    counter+=1
                answer = max(answer, counter)

        return answer