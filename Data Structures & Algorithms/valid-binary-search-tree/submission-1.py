# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        preorder = []
        
        def dfs(curr):
            if curr is None:
                return

            dfs(curr.left)
            preorder.append(curr.val)
            dfs(curr.right)

        dfs(root)
        
        for i in range(1,len(preorder)):
            if preorder[i] <= preorder[i-1]:
                return False

        return True
            