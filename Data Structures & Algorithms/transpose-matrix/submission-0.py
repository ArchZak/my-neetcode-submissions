class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #input: a 2d array of integers
        #output: the transpose of that matrix, doesnt have to be in place

        #transposing a matrix is basically making the row a col, so 1st row becomes 1st col
        #so going to create a new array that is the correct dimensions
        #then going to loop through given matrix and put new numbers in

        transpose = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose[j][i] = matrix[i][j]

        return transpose