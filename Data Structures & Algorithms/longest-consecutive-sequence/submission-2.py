class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        hash_set = set()
        counter = 0

        for num in nums:
            if num-1 in hash_set:
                hash_set.add(num)
            else:
                counter = max(counter,len(hash_set))
                hash_set= set([num])

        return max(counter,len(hash_set))