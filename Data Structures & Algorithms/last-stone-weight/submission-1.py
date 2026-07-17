class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #input: array of ints where i is weight of that stone
        #output: weight of last stone after simulation

        #each step, we take 2 heaviest, if x==y(both gone), if x < y, x gone and y-=x
        #do steps until only 1 stone is left, if none left then return 0

        #use a max heap to easily pop off and push stones on
        #take two off at each step and keeping going while len > 1
        stones = [-x for x in stones]
        heapq.heapify(stones) #native minheap so we do - to make it max
        while len(stones) > 1:
            x, y = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
            if x == y:
                continue
            else:
                heapq.heappush(stones, -1*(abs(x-y)))

        return 0 if not stones else stones[0]*-1