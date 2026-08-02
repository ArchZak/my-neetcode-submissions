class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input: array of integers and an int h
        #output: minimum int to get through array in h time

        #array if int is piles of bananas, and h is hours to eat all bananas
        #so what is the minimum k to eat all the bananas in h hours

        #brute force would be to loop through each num up to the biggest num in the array
        #until we find the first that works
        #so instead we can use binary search on the range of ints

        left, right = 1, max(piles)
        answer = max(piles)

        while left <= right:
            mid = (left+right)//2
            print(mid, left, right)
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid) #calculating how much time it takes to eat a pile
            if time > h:
                left = mid+1
            else:
                # idk what to do here
                right = mid-1
                answer = min(mid, answer)
        
        return answer