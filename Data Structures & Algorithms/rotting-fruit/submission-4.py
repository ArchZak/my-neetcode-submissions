class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #input: 2d array of ints where vlaues are 0(empty), 1(fresh), 2(rotten)
        #output: minimum mins after array becomes 100% rotten, if not possible give -1

        #every min, if fresh fruit is hori/vert to rotten fruit, it becomes rotten

        #need to find all rotten fruit and then add their coords to queue
        #then need to do bfs through graph going up down left right
        #append neighbor to queue if it's fresh fruit + in bounds
        #count the minutes per iteration
        #then do a final check to see if any fresh fruit survived 

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque([])
        answer = 0
        fruit = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.appendleft((i,j))
                elif grid[i][j] == 1:
                    fruit+=1

        while queue and fruit:
            for _ in range(len(queue)):
                curri, currj = queue.pop()
                for diri, dirj in directions:
                    newi, newj = curri+diri, currj+dirj
                    if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and grid[newi][newj] == 1:
                        queue.appendleft((newi,newj))
                        grid[newi][newj] = 2
                        fruit-=1
            answer+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return answer