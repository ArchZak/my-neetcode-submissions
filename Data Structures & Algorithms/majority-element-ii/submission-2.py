class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        import math
        tracker = {}
        answer = []

        for num in nums:
            tracker[num] = tracker.get(num,0)+1

        for key, value in tracker.items():
            if value > len(nums)/3:
                answer.append(key)

        return answer