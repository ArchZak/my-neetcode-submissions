class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #input: 2d array of ints where -1 is water(cant go on), 0 is treasure, INF is normal land
        #output: same 2d array but replace INF with distances to nearest treasure if possible, otw INF

        #going to use bfs where you start it on inf tiles
        #bfs through 2d array and whenever you find a tresure, return the number of steps

        #bfs needs init directions of up, down, left, right
        #while you have queue, for each item in the queue, cycle its directions and add neighbors

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(i,j):
            queue = deque([(i,j)])
            tracker = set()
            steps = 0

            while queue:
                for _ in range(len(queue)):
                    i1, j1 = queue.popleft()
                    if grid[i1][j1] == 0:
                        return steps
                    for di, dj in directions:
                        i2, j2 = i1+di, j1+dj
                        # if not out of bounds, not alr visited, and not water
                        if (0 <= i2 and 0 <= j2 and i2 < len(grid) and j2 < len(grid[0]) and (i2,j2) not in tracker and grid[i2][j2] != -1):
                            tracker.add((i2,j2))
                            queue.append((i2,j2))
                    
                steps+=1

            return 2147483647

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)


        