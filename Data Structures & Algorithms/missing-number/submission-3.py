class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #input: a list of ints where it has n ints ranging 0,n without dupes
        #output: return the single num in the range that is missing

        #add the curr index, sub the value at the curr index
        #basically summing up the whole array and then removing the values

        answer = -sum(nums)
        for i in range(len(nums)+1):
            answer+=i
            print(answer)
        return answer