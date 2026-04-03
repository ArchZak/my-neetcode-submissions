# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global answer
        answer = []

        def dfs(curr):
            if curr == None:
                return

            dfs(curr.left)
            dfs(curr.right)
            answer.append(curr.val)

        dfs(root)
        return answer