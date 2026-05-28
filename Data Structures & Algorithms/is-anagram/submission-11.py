class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = defaultdict(int)

        for letter in s:
            tracker[letter]+=1

        for letter in t:
            tracker[letter]-=1

        for key, value in tracker.items():
            if value != 0:
                return False

        return True

