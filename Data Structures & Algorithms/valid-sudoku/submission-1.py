class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_tracker = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in row_tracker:
                    return False
                else:
                    row_tracker.add(board[row][i])

        for col in range(9):
            col_tracker = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in col_tracker:
                    return False
                else:
                    col_tracker.add(board[i][col])

        for box in range(9):
            box_tracker = set()
            for i in range(3):
                for j in range(3):
                    row = (box//3) * 3 + i
                    col = (box % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in box_tracker:
                        return False
                    box_tracker.add(board[row][col])

        

        return True
