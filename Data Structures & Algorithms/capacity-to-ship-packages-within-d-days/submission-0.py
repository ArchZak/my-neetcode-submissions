class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #input: array of ints for weights and an int for days target
        #output: minimum weight capacity of the ship

        #so the weights are like a queue, we load them up in order
        #we dont want the weights to be more than the max weight of capacity 
        #we want to return the least capacity of the ship

        #going to do binary search on max weight as left and them the sum of all the values right
        #this way we never have to worry about the ship going over capacity since it isnt possible bc the lower range being the max value

        #need to loop through weights array and count how many times we reach max capacity

        
        #if we took too many days, move left up 
        #if we had time to spare, take the min answer
        #eventually return the answer which is the min weight

        left, right = max(weights), sum(weights)
        answer = right

        while left <= right:
            mid = (left+right)//2
            time = 1
            curr = 0
            for i in range(len(weights)):
                if curr+weights[i] > mid:
                    time+=1
                    curr = 0
                curr+=weights[i]
            if time > days: #took too long
                left = mid+1
            else:
                answer = min(answer,mid)
                right = mid-1

        return answer
