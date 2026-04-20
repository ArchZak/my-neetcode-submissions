class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        import copy
        temp = copy.deepcopy(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[j][i] = temp[i][j]

        for k in range(len(matrix)):
            matrix[k].reverse()