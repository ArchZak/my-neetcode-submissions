class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        #input: positive int n 
        #output: n x n matrix with the spiral order of 1->n^2

        #need 4 pointers, top bottom left right
        #top and left will be 0, bottom and right will be len(matrix), len(matrix[0])
        #going to use it to loop through in spiral order
        
        #while left < right and top < bottom:
        #   loop towards right and place values
        #   top++
        #   loop towards bottom and place values
        #   right--
        #   loop towards left and place values
        #   bottom--
        #   loop towards top and place values
        #   left++

        #test case: 
        #1 = [[1]]
        #3 = [[1,2,3],[4,5,6],[7,8,9]]

        #n will be at least 1, at most 20

        curr = 1
        matrix = [[0]*n for _ in range(n)]
        left, top = 0, 0
        right, bottom = len(matrix[0]), len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                matrix[top][i] = curr
                curr+=1
            top+=1

            for i in range(top, bottom):
                matrix[i][right-1] = curr
                curr+=1
            right-=1

            if not (left < right and top < bottom):
                break

            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = curr
                curr+=1
            bottom-=1

            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = curr
                curr+=1
            left+=1

        return matrix
