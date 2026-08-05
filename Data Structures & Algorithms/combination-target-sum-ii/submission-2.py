class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #input: array of ints (may have dupes) and a target int
        #output: all the unique combos of ints that add up to target

        #can only choose each element from array at most one time
        #cant have dups

        #going to do dfs where you either skip int or append and then move on
        #base case: if at target then add to answer and return
        #base case: if over target or out of bounds then return 
        #so dfs is either append and go next or just go next

        answer = []
        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                answer.append(curr.copy())
                return
            if len(candidates) <= i or curr_sum > target:
                return

            curr.append(candidates[i])
            dfs(i+1,curr,curr_sum+candidates[i])
            curr.pop()
            #skip dupes
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr, curr_sum)

        candidates.sort()
        dfs(0,[], 0)
        return answer
