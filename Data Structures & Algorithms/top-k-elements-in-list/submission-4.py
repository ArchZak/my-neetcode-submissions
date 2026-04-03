class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict={}
        answer=[]
        bucket=[[] for i in range(len(nums)+1)]

        for num in nums:
            counter_dict[num]=counter_dict.get(num,0)+1

        for index, counter in counter_dict.items():
            bucket[counter].append(index)

        for i in range(len(bucket)-1,0,-1):
            while len(answer) < k and len(bucket[i]) > 0:
                answer.append(bucket[i].pop())

        return answer
