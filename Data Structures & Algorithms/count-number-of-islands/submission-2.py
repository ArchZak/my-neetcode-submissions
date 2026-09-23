class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input: 2d array of '1' and '0' where 1 is land and 0 is water
        #output: count number of islands

        #island is formed by connectring adjacent lands hori and vert and is surrounded by water
        #anything outside the 2d array is water so don't worry about it

        #need to dfs through the array based on land we haven't seen
        #if we find an island, dfs through the whole thing and then we track 1 island
        #eventually we'll loop through the whole grid and have found each island

        #constraints: at least 1x1, can be 100x100
        #either 0 or 1 for [i][j]

        #dfs(i,j)
        #check if in bounds + havent visisted, or if water: if not return
        #append curr coords in seen
        #dfs to up down left right

        #for i in range
            #for j in range
                #start dfs if we havent seen this 1 before
                #increment answer by 1

        visited = set()
        answer=0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i,j) in visited or grid[i][j] == '0':
                return
            visited.add((i,j))

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    answer+=1

        return answer

        