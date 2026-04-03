class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict={}
        counter_freq=[[] for i in range(len(nums)+1)]
        answer = []

        for num in nums:
            counter_dict[num]=1+counter_dict.get(num,0) #.get will be 0 if it doesnt exist

        for num, freq in counter_dict.items():
            counter_freq[freq].append(num)

        for i in range(len(counter_freq)-1,0,-1):
            for num in counter_freq[i]:
                answer.append(num)
                if len(answer) >= k:
                    return answer