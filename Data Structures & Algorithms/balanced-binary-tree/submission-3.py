# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #input: a binary tree
        #output: true if height balanced (false otw)
        #meaning each node in a binary tree, left and right subtrees dont differ in height in more than 1 node

        #run dfs on each subtree for height 
        #base case: if null, return 0
        #recur case: return max(left,right) + 1

        #compare subtree height
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