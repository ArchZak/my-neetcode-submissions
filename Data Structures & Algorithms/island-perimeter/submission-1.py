class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #input: 2d array of ints where 1 is an island
        #output: the perimeter of the island 

        #dfs through the array and visit if 1
        #check the sides, if it is 0 or out of bounds, add 1 for perimeter
        #track locations so we dont bounce backwards

        tracker = set()

        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i,j) in tracker:
                return 0
            tracker.add((i,j))

            answer = dfs(i+1,j)
            answer += dfs(i-1,j)
            answer += dfs(i,j+1)
            answer += dfs(i,j-1)

            return answer

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)