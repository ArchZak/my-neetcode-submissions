# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #input: bst and int k where we want kth index (1 indexed)
        #output: kth smallest index 
        self.answer = []

        def dfs(curr):
            if curr is None:
                return
            
            dfs(curr.left)
            self.answer.append(curr.val)
            dfs(curr.right)

        dfs(root)
        return self.answer[k-1]