class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: int array nums, return k most freq elems in array
        # bucket sort: values are [] with numbers, keys are occurrences
        # dict: key is the number, value will the occurences 

        # one loop for our dictionary
        # one loop for our bucket sort array -> loop by array value, then append key to [] at index
        # another loop for getting the answer with k

        #ASK ABOUT EDGE CASES

        bucket_sort = [[] for _ in range(len(nums)+1)]
        helper={}
        answer=[]

        for num in nums:
            helper[num] = helper.get(num,0)+1 #tracks occurrences of nums

        for key, value in helper.items():
            bucket_sort[value].append(key) #bucket sorts ^^

        #loop backwards through bucket sort
        #while loop through each input

        for i in range(len(nums),-1,-1): #start at end of array, go down to 0, step down 1 at a time
            bucket_values = bucket_sort[i]
            for num in bucket_values:
                if len(answer) < k:
                    answer.append(num)

        return answer
