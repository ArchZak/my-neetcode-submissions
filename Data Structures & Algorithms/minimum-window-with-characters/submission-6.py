class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #input: two strings s and t
        #output: substring of s that has every char in t(including dupes), or "" if DNE

        #gonna do immeidate check for len t > s
        #otherwise gonna make a dict of letter in t: count

        #going to do a for loop to start on letter
        #while loop to start decrementing tracker and count loop
        
        # answer = len(s)
        answer = ""
        curr_min = len(s)
        i = 0
        for index, letter in enumerate(s):
            counter = 0
            tracker = Counter(t)
            while index+counter<len(s) and any(tracker.values()):
                if s[index+counter] in tracker:
                    tracker[s[index+counter]]-=1 if tracker[s[index+counter]] > 0 else 0
                counter+=1
            if not any(tracker.values()):
                if counter <= curr_min:
                    curr_min = counter
                    i = index
                    answer = s[i:i+curr_min]

        return answer