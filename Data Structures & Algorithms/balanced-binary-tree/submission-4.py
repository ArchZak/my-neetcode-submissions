# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #input: root of binrary tree 
        #output: true if height balanced, false if otw

        #hieght balanced means all left and right subtrees differ by no more than 1 height

        #want to dfs through tree, then dfs on each node to check subtree heights
        #if its ever false, change the global variable
        #want to compare left and right of node
        
        self.answer = True

        def dfs(curr):
            if curr is None:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left-right) > 1:
                self.answer = False

            return max(left,right)+1

        dfs(root)
        return self.answer
