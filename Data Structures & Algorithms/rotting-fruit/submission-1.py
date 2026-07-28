class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Input: 2d array of ints where cells are 0(empty) tile 1(fresh) fruit 2(rotten) fruit
        #output: minimum number of minutes to elapse where there are 0 fresh fruit (-1 if impossible)

        #every min, if fresh fruit is hori or vert adj to rotten fruit, it becomes rotten too
        #need to find all rotten fruit in the grid and add them to queue 
        #init a minute + queue + tracker
        #while we have a queue, for each item in the queue, check if fresh, if so, add it to seen and make it rotten
        #when we're done with bfs check grid to see if there are fresh fruit left, if so, -1, if not, return minute

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        tracker = set()
        queue = deque([])
        minutes = 0
        bfsd = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    tracker.add((i,j))

        while queue:
            bfsd = True
            for _ in range(len(queue)):
                i1, j1 = queue.popleft()
                if grid[i1][j1] == 1:
                    grid[i1][j1] = 2
                for di, dj in directions:
                    i2 = i1+di
                    j2 = j1+dj
                    # if in bounds and not visited and not empty
                    if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and (i2,j2) not in tracker and grid[i2][j2] != 0:
                        queue.append((i2,j2))
                        tracker.add((i2,j2)) 

            minutes+=1

        if bfsd:
            minutes-=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes