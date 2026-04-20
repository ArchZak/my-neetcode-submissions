class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #input: m x n matrix of ints where if elm is 0, set entire row and cols to 0
        #output: matrix needs to be changed in place and with O(1) space

        #track what rows and cols have 0s in their own sets
        #after finding which rows and cols have 0s, loop through each and set to 0

        cols_tracker, rows_tracker = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    cols_tracker.add(j)
                    rows_tracker.add(i)

        i=0
        for row in rows_tracker:
            for i in range(len(matrix[row])):
                matrix[row][i] = 0

        i=0
        for col in cols_tracker:
            for i in range(len(matrix)):
                matrix[i][col] = 0


        