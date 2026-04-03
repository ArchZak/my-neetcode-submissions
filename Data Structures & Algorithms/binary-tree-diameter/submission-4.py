# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #input: a binary tree
        #output: diameter = the longest path between ANY two nodes in the binary tree

        #run the height operation on every subtree in the binary tree
        #can do that with a dfs and have a global variable that tracks the biggest diameter

        self.answer = 0
        #base case: return 0 if null
        #recursive case: return +1 max left or right 
        def dfs(curr):
            if curr == None:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.answer = max(self.answer, left+right)
            return max(left,right)+1

        dfs(root)
        return self.answer

