class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #input: 2d array if ints where -1 is water(cant go on it), 0 is treasure, INF is land
        #output: the same 2d array but INF is distance to nearest treasure if possible

        #going to use bfs
        #start bfs on every tile that is INF so we can bfs until we find a treasure, or the entire grid
        #while queue, for each item in the queue, check if we found land, if not, add the up, down, left, right
        #cycle through up down left right on another for loop with directions
        #have set to track locations throughout the bfs, sep done

        #the idea is we traverse from that point until we find something
        #and we add the neighbors of the curr i,j 
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(i,j):
            tracker = set()
            step = 0
            queue = deque([(i,j)])

            while queue:
                for _ in range(len(queue)):
                    i1, j1 = queue.popleft()
                    if grid[i1][j1] == 0:
                        return step
                    for di, dj in directions:
                        i2, j2 = i1+di, j1+dj
                        # if in bounds and not visited and not water, add neighbor to queue
                        if i2 >= 0 and j2 >= 0 and i2 < len(grid) and j2 < len(grid[0]) and (i2,j2) not in tracker and grid[i2][j2] != -1:
                            queue.append((i2,j2))
                            tracker.add((i2,j2)) 

                step+=1
            return 2147483647

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)