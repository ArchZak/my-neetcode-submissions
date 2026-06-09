class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracking = defaultdict(int)

        for letter in s:
            tracking[letter]+=1

        for letter in t:
            tracking[letter]-=1

        for num in tracking.values():
            if num != 0:
                return False

        return True