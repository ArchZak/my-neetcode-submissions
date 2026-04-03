class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #array of people where one is secretly the judge
        #town judge trusts nobody
        #everyone trusts the town judge
        #only one person is 1 and 2

        #given n where n is n people
        #given array where trust[i] is [ai,bi] where ai trusts bi

        #return label of town judge or -1 if he doesnt exist

        #should loop through array of trust
        #have helper tracker that is n+1 long
        #++ 1 to index that is trusted and --1 if person trusts
        #return the first index we find that is == n-1 (everyone but himself)

        tracker = [0]*(n+1)
        for ai, bi in trust:
            tracker[ai]-=1
            tracker[bi]+=1

        for i, num in enumerate(tracker):
            if num == n-1: 
                return i
        return -1