class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tracker = [0]*(n+1)
        for ai, bi in trust:
            tracker[ai]-=1
            tracker[bi]+=1

        for i, num in enumerate(tracker):
            if num == n-1: 
                return i
        return -1