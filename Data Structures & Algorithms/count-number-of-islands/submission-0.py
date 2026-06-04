class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input: 2d array of strings that are either 0(water) or 1(land)
        #output: the number of islands in the 2d array

        #need a data structure to track the coords visited
        #dfs through the 2d array, if out of bounds, or not land, base case
        #otw travel to another space, up, down, left, right
        #add the coord in obv to remember, and then everytime we exit, add one to answer

        answer = 0
        tracker = set()

        def dfs(i,j):
            if len(grid) <= i or len(grid[0]) <= j or i < 0 or j < 0 or (i,j) in tracker or grid[i][j] == "0":
                return
            
            tracker.add((i,j))

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in tracker:
                    dfs(i,j)
                    answer+=1

        return answer