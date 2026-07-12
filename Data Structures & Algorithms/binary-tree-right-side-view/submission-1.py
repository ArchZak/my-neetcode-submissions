# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #input: root of a binary tree
        #output: list of nodes only visible from right side

        #want to dfs down right side of tree and track height
        #we have a list to store answers in
        #if height == len(list) than we need to add new right side node

        answer = []
        def dfs(curr, height):
            if curr is None:
                return None
            if height == len(answer):
                answer.append(curr.val)
            
            dfs(curr.right, height+1)
            dfs(curr.left, height+1)

        dfs(root, 0)
        return answer
