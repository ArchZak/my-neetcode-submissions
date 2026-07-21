# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def dfs(curr, height):
            if curr == None:
                return 0

            left = dfs(curr.left, height+1)
            right = dfs(curr.right, height+1)
            self.answer = max(left+right, self.answer)
            return 1+max(left, right)

        dfs(root, 0)
        return self.answer