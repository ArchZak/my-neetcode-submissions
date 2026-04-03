class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        sorted_counter = dict(sorted(counter.items(), key=lambda c: c[1], reverse=True))
        
        answer = [0]*k
        for index, val in enumerate(sorted_counter.keys()):
            if index < k:
                answer[index] = val
            else:
                return answer
        return answer



        
        
        

        