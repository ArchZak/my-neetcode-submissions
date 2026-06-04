class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #input: 2d array of integers
        #output: the are of the biggest island in the grid

        #going to dfs through the 2d grid
        #while dfsing, gonna track the number of grids added to the tracking set of coords
        #need to double for loop through grtid to start on each 1 not seen
        #then gonna record len before going in, and then take max of new len

        tracker = set()
        answer = 0

        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or (i,j) in tracker or grid[i][j] != 1:
                return
            tracker.add((i,j))
            self.area+=1

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in tracker:
                    self.area = 0
                    dfs(i,j)
                    answer = max(answer, self.area)

        return answer