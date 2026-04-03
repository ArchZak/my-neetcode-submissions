class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #input: array of ints stones where stone[i] is weight of ith stone
        #output: return heaviest stone if remaining, or 0 if none

        #simulation:
        #choose two heaviest stones at each step, with weight x and y
        #if x==y, both stones are destroyed
        #if x<y, then stone x is destroyed and stone y has new weight of y-x

        #continue sim until there is no more than 1 stone remaining

        #so heapify the array to start
        #use nlargest for the two largest stones -> check return length before operating
        #do the abs(x-y) ops for them
        #if statements based on output
        #push new rock back on queue if needed

        stones = [-x for x in stones]

        heapq.heapify(stones)

        while stones:
            heavy_stones = heapq.nsmallest(2, stones)
            if not heavy_stones:
                return 0
            elif len(heavy_stones) == 1:
                return -heavy_stones[0]
            else:
                x = -heapq.heappop(stones)
                y = -heapq.heappop(stones)
                new_stone = abs(x-y)
                heapq.heappush(stones, -new_stone)

        return 0
                