# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #input: given root of a binary tree and int k
        #output: output kth smallest val that is 1-indexed in tree

        #dfs through tree with post order tracking and then return the k+1 val

        self.array = []
        def dfs(curr):
            if curr is None:
                return 

            dfs(curr.left)
            self.array.append(curr.val)
            dfs(curr.right)
        
        dfs(root)
        return self.array[k-1]
            