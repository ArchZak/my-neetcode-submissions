class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #input: a 2d array of integers
        #output: a target int

        #binary search through the matrix
        #binary search through rows, then binary search in row found

        #rows are sorted so anything after last index is greater
        #so we should do comparison ops on last value in array
        left, right = 0, len(matrix)-1
        while left <= right:
            mid = (left+right)//2
            if matrix[mid][-1] < target:
                left = mid+1
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                break
        
        row = matrix[mid]
        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid = (left+right)//2
            if row[mid] < target:
                left = mid+1
            elif row[mid] > target:
                right = mid-1
            else:
                return True

        return False
