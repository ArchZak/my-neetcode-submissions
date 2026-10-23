class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        given array of n ints in the range [0,n] with no dupes
        return the single number in the range that is missing from nums

        solve in constant space + linear runtime

        numbers will be positive
        wont be sorted, always
        will have at least 1 num

        sort:
            then count until you find the missing: nlogn time, const space

        count:
            you sum the whole nums but negated
            you add every num up to the length
            wtv we are missing is the answer
        """

        answer = -sum(nums)
        for i in range(len(nums)+1):
            answer+=i
        return answer