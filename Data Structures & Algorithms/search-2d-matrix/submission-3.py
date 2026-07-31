class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #input: a 2d array of ints that are sorted, and a target int
        #output: whether or not the target is in the matrix

        #need to write this in log(m*n)
        #so need to binary search the rows, and when we find our row, binary search the array
        #compare the last num in the rows when doing the first one
        
        left, right = 0, len(matrix)-1
        while left <= right:
            mid = (left+right)//2
            if matrix[mid][-1] < target:
                left = mid+1
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                break

        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid1 = (left+right)//2
            if matrix[mid][mid1] < target:
                left = mid1+1
            elif matrix[mid][mid1] > target:
                right = mid1-1
            else:
                return True

        return False