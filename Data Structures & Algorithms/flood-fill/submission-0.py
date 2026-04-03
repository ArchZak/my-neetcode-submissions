class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #want to flood fill a 2d array starting at image[sr][sc]
        #1) begin with starting pixel and change its color to colors
        #2) perform same process for each directly adjacent pixel that's same color as starting
        #3) keep repeating until there are no more adjcaent pixels of original color
        
        #input: image 2d array, sr, sc, new color
        #output: new 2d array with flood fill

        #want to dfs through image
        #need to check if adjacent is in bounds + same color
        #then change color and dfs to around

        if image[sr][sc] == color:
            return image

        og_color = image[sr][sc]

        def dfs(m, n):
            if m < 0 or m > len(image)-1 or n < 0 or n > len(image[m])-1: #bounds
                return
            if image[m][n] != og_color: #if not og color, ignore
                return

            image[m][n] = color

            dfs(m-1,n)
            dfs(m+1,n)
            dfs(m,n+1)
            dfs(m,n-1)

        dfs(sr,sc)
        return image
