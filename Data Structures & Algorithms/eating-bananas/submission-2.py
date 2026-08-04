class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input: array of integers and an int h
        #output: minimum int to get through all ints in array in h iterations

        #given int array piles where i is number of bananas in pile i
        #also given int h where it reps hours i have to eat the bananas in each pile
        #have to decide the minimum bananas per hour eating rate we can have
        #you can eat k bananas from 1 pile per hour

        #could just test each int until we find one that works
        #or we can do binary search on the max pile size in piles and 1
        #for each iteration, we then check to see if we fit
        #if we didnt finish the pile in time, move left up
        #if we finished the pile with time to spare, take the min answer

        left, right = 1, max(piles)
        answer = right

        while left <= right:
            mid = (left+right)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid) #if mid 2 and pile 5, should take 3. wont trun
            if time > h: #so if we took too long
                left = mid+1
            else:
                answer = min(answer, mid)
                right = mid-1

        return answer