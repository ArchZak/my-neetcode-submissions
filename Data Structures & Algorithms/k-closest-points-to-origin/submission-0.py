class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #input: 2d array points where points[i]=[xi,yi], also given k
        #output: return the k closest points to the origin

        #dist = (sqrt((x1 - x2)^2 + (y1 - y2)^2))
        #dist = sqrt(x**2+y**2) -> programming logic

        #constraints: k is <= array.length
        #values for points can be negative or positive

        #use a heap here using heapq
        #loop through points, and push [dist,x,y] to our heap
        #then just return nsmallest(k, heap)

        heap = []
        answer = []

        for point in points:
            x, y = point[0], point[1]
            dist = (x**2+y**2)**(1/2)

            heapq.heappush(heap, [dist,x,y])

        biggest = heapq.nsmallest(k, heap)

        return [x[1:] for x in biggest]

        
