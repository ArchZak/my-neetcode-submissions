# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #input: tree and subtree
        #output: if subtree is a subtree a tree

        #if subtree is none, true
        #if subtree isnt none, and tree is none, false
        #check current node, then send off left or right
        #helper func, dfs
        #base case is if both are null, true
        #if both exist + both are equal, then check dfs
        #otw false

        def helper(curr, sub_curr):
            if curr is None and sub_curr is None:
                return True
            if curr and sub_curr and curr.val == sub_curr.val:
                return helper(curr.left, sub_curr.left) and helper(curr.right, sub_curr.right)
            return False

        if subRoot is None:
            return True
        if root is None:
            return False

        if helper(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
