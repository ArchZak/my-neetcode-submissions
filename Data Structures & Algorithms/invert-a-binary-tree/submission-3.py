# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #given the root of a binary tree, invert it and return the root
        #need to dfs through the tree and swap the children of each node around

        def dfs(curr):
            if curr is None: #base case
                return
            
            dfs(curr.left)
            dfs(curr.right)

            temp = curr.left
            curr.left = curr.right
            curr.right = temp

            return curr

        return dfs(root)