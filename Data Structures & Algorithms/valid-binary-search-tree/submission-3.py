# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #input: root of a binary tree
        #output: whether or not a binary tree is valid or not

        #do a in order traversal of the tree
        #if a sorted version of the array is diff, return false
        self.array = []
        def dfs(curr):
            if curr is None:
                return
            
            dfs(curr.left)
            self.array.append(curr.val)
            dfs(curr.right)

        dfs(root)
        return sorted(list(set(self.array))) == self.array
