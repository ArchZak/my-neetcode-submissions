# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global answer
        answer = []

        def dfs(curr):
            if curr == None:
                return

            dfs(curr.left)
            answer.append(curr.val)
            dfs(curr.right)

        dfs(root)
        return answer
