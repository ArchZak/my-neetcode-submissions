class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        helper = {}

        for num in nums:
            helper[num] = helper.get(num,0)+1

        answer = 0
        counter = 0
        for key, value in helper.items():
            if counter < value:
                counter = value
                answer = key

        return answer

        