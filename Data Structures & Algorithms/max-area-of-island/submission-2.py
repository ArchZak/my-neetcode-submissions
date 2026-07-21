class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #input: 2d array of integers of 0s and 1s
        #output: area of the largest island of 1s

        #the outside of the grid is water

        land_tracker = set()
        self.temp, answer = 0, 0

        def dfs(i,j):
            #if out of bounds or water or alr visited
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or (i,j) in land_tracker:
                return

            land_tracker.add((i,j))
            self.temp+=1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in land_tracker:
                    self.temp = 0
                    dfs(i,j)
                    answer = max(answer, self.temp)

        return answer