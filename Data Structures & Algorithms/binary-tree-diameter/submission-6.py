# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        #input: root of tree
        #diameter is length of longest path between any two nodes, not necessarily root
        #output: diameter of the tree

        #do height dfs on each node and store it in global var

        def dfs(curr):
            if curr is None:
                return 0

            left = dfs(curr.left)            
            right = dfs(curr.right)            

            self.answer = max(self.answer,left+right)
            return max(right,left)+1

        dfs(root)
        return self.answer