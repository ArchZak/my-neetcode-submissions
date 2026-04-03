class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for l in range(len(s2)):
            s1_set = list(s1)
            r=l
            while r < len(s2) and s2[r] in s1_set and r < r+len(s1):
                s1_set.remove(s2[r])
                r+=1
                if len(s1_set) == 0:
                    return True

        return False