# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global answer
        answer = []

        def dfs(curr):
            if curr == None:
                return

            answer.append(curr.val)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return answer