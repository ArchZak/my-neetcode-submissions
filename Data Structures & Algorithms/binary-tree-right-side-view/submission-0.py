# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #input: root of a BST
        #output: list of vals visible from right side of tree ordered top down

        #want to dfs down the right side of the tree and track the height
        #want a list to store the answers in
        #if the len of the list is equal to the hieght we're at, we find a new node on the right

        answer = []

        def dfs(curr, height):
            if curr is None:
                return

            if len(answer) == height:
                answer.append(curr.val)
            
            dfs(curr.right, height+1)
            dfs(curr.left, height+1)

        dfs(root, 0)
        return answer