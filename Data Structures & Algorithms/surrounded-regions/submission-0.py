class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #input: a 2d array containing X and O 
        #output: the smae 2d array but with captured regions (so surround)

        #a cell is connected hori and vert
        #to form a region, connect every O cell, prob gonna dfs through it
        #a region is surrounded if none of the O cells in the region are on the edge of the board
        # ^^ so completely enclosed by X
        #to capture a region, replace all the Os with Xs in place, return nothing

        #so need to do double for loop to find Os
        #if we find an O, start doing dfs on that point to try and find out of border
        #so we want two sep statements, one for border detect, one for X
        #track all coords using set, if we come across a border, set a bool to leave them alone
        #otw convert them all

        safe_region = set() #set to have coords you cant take over
        temp = set()

        def dfs(i2,j2):
            #so if out of bounds
            if i2 < 0 or j2 < 0 or i2 > len(board)-1 or j2 > len(board[0])-1:
                self.safe = True
                return
            #if not part of region
            if board[i2][j2] == 'X' or (i2,j2) in temp:
                return

            temp.add((i2,j2))
            dfs(i2+1,j2)
            dfs(i2-1,j2)
            dfs(i2,j2+1)
            dfs(i2,j2-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in safe_region:
                    temp = set() #set for potential conversion
                    self.safe = False
                    dfs(i,j)
                    if self.safe:
                        safe_region|=temp
                    else:
                        for i1, j1 in temp:
                            board[i1][j1] = 'X'


            
            