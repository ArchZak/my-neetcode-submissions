class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #input: list of nums and a target integer
        #output: the unique combinations of nums where chosen nums sum to target

        #you can pick the same number an unlimited amount of times
        #combinations are the same if the freq of the chosen nums is the same
        #can return the combinations in any order and the order of the nums can be in any order

        #going to traverse through the array recursively
        #either gonna continue on curr index or skip to next index in nums
        #base case: if target met, exit out
        #base case: if over target or out of bounds, exit out
        #do curr index or next index
        import copy

        answer = []

        #i is curr index, curr is array we have rn of combos
        def traverse(i, curr):
            if sum(curr) == target:
                answer.append(copy.deepcopy(curr))
                return
            if sum(curr) > target or len(nums) <= i:
                return

            curr.append(nums[i])
            traverse(i, curr)
            curr.pop()
            traverse(i+1, curr)

        traverse(0, [])
        return answer
