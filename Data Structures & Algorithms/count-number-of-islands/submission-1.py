class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input: 2d array of ints where '1' is land and '0' is water
        #output: number of islands in the 2d array

        #island is formed by land that's hori and vert and surrounded by water
        #stuff outside the grid is water so at least 1 island if you find land

        #going to double for loop through array and find land
        #then dfs through the land and add coords to a set so we dont double dip

        land_tracker = set()
        answer = 0
        def dfs(x, y):
            #if out of bounds or water or alr visited
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0' or (x,y) in land_tracker:
                return

            land_tracker.add((x,y))
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in land_tracker and grid[i][j] == '1':
                    dfs(i,j)
                    answer+=1

        return answer