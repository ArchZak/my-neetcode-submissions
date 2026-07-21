# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #input: root of a binary tree
        #output: max path sum through tree

        #need to do dfs when finding largest path
        #instead of passing height around, pass the path sum so far

        self.answer = root.val
        def dfs(curr, path):
            if curr == None:
                return 0

            left = max(dfs(curr.left, path+curr.val),0)
            right = max(dfs(curr.right, path+curr.val),0)
            self.answer = max(self.answer, left+right++curr.val)
            return max(left,right)+curr.val

        dfs(root, root.val)
        return self.answer