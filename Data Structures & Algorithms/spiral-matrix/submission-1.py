class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #input: m x n matrix of ints
        #output: the 2d array but in spiral order

        #going to have 4 pointers at the top bottom right and left
        #left and top are gonna be 0, right and bottom are gonna be len
        #going to loop in spiral fashion

        #while pointers arent same int
            #gonna loop forward on curr row
            #top++
            #gonna loop down on curr column
            #right--
            #gonna loop backward on new row
            #bottom--
            #gonna loop up on new column
            #left++

        #whenever we have pointers overlap then we stop iterating
        #matrix will be at least 1 x 1 length 

        #ex test case :[[1]], [[1,2],[3,4]], [[1,2,3],[1,2,3],[1,2,3]]
        #should return 1, 1-2-4-3, 1-2-3-3-3-2-1-1-2

        left, top = 0, 0
        right, bottom = len(matrix[0]), len(matrix)
        answer = []

        while left < right and top < bottom:
            for i in range(left, right):
                answer.append(matrix[top][i])
            top+=1
            for i in range(top, bottom):
                answer.append(matrix[i][right-1])
            right-=1
            if not (left < right and top < bottom):
                break
            for i in range(right-1, left-1, -1):
                answer.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1, top-1, -1):
                answer.append(matrix[i][left])
            left+=1

        return answer


