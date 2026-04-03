# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #input: two binary trees
        #output: true is the trees are equiv, false if otherwise

        #dfs where we compare each node in both trees togther
        #global variable set to true

        self.answer = True

        def dfs(curr1, curr2):
            if curr1 == None and curr2 == None: #both are null
                return
            if curr1 and curr2: #both are nodes
                if curr1.val != curr2.val:
                    self.answer = False
                dfs(curr1.left, curr2.left)
                dfs(curr1.right, curr2.right)
            else:
                self.answer = False
                return
            
        dfs(p,q)
        return self.answer

