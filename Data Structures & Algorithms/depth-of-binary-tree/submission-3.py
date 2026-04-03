# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #input: root of a binary tree
        #output: the depth of said tree

        #depth = root -> farthest leaf
        #dfs, traverse down the tree
        #hit a null, then return 0, then cascade up +1s with our recursive case

        if root == None:
            return 0

        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1