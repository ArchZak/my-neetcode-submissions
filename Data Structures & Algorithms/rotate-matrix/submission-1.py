class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #input: 2d array of ints
        #output: the same matrix but everything is rotated 90 degrees

        #need a second matrix that's a deep copy
        #then need to use that matrix to write to second matrix where 1st row is last col for ex

        new_matrix = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[i][j] = matrix[i][j]

        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                matrix[j][len(matrix[0])-1-i] = new_matrix[i][j]
