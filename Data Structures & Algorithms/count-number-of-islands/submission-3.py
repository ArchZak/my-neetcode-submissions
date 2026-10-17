class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input:#2d array grid of '1' == land and '0' == water
        #output:#need to cound and return number of islands

        #general
        #island being formed by connecting adjacent lands hori/vert(up down left right) + surr by water
        #anything aoutside the array is water

        #constraints + edge cases
        #will have at least 1 character in the grid, 1x1 to 100x100
        #can only access island via up down left right
        #anything outside array is water

        #tests + examples: dfs or bfs
        # Input: grid = [
        #     ["1","0","0","0","0"],
        #     ["0","1","0","0","0"],
        #     ["0","0","1","0","0"],
        #     ["0","0","0","1","0"]
        # ]
        # Output: 4 (could use dundername to call func but yk, neetcode)

        #english + pseudo
        #need to find an array to start traversal
        #then we can dfs through, 1) track visit in set 2) can turn 1 to 0 while lookin
        #when we exit the traverse, then we can ++ answer

        #dfs(i,j):
        #   if out of bounds or if 0, return
        #   if not ^^, then turn curr to 0
        #   then go up down left right
        #double for loop to check each spot
        row, col, answer = len(grid), len(grid[0]), 0

        def dfs(i,j):
            if i >= row or i < 0 or j >= col or j < 0 or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i,j)
                    answer+=1

        return answer
