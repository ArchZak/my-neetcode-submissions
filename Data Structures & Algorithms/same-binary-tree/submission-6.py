# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #given two trees p and q, want to return whether theyre true or not
        #can dfs through the trees and then compare the nodes at that tree
        #if a node is different, or a node exists in one tree and not the other, it's false

        self.answer = True

        def dfs(curr1,curr2):
            if curr1 is None and curr2 is None:
                return
            if curr1 and curr2 and curr1.val == curr2.val:
                dfs(curr1.left, curr2.left)
                dfs(curr1.right, curr2.right)
            else:
                self.answer = False
                return

        dfs(p,q)
        return self.answer
        