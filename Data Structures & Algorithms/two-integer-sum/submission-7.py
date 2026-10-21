class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input: given array of ints + target int
        #output: return indices make target such that i != j, smaller index first

        #general
        #hashmap tldr

        #constraints + edge cases
        #can assume every input has exactly 1 solution to satisfy condition
        #so array will be at least len two, values can be whatever
        #Only 1 solution should exist, doesnt matter rn tho

        #solution: need to hashmap
        #going to loop through the array
        #for each value, detect what value we need left to get target
        #so we will have the hashmap be: {} where value remaining: the index from before
        #smaller index first

        #test + examples
        #[3,6,5,4], target = 7. answer = [0,3]
        #{4:0,1:1,2:2}

        hashmap = {}
        for index, num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], index]
            hashmap[target-num] = index