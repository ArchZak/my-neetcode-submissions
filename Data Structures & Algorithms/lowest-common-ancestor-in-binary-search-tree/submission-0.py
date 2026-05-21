# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #input: actual tree, and then two nodes
        #output: lowest node that is common ancestor of both nodes

        #want to traverse through the tree
        #if the node is less than one node and greater than the other, it's the answer
        #if node is equal to one of the nodes, it's the answer

        def dfs(curr):
            if curr == None:
                return
            elif ((curr.val <= p.val) or (curr.val <= q.val)) and ((curr.val >= p.val) or (curr.val >= q.val)):
                return curr
            elif (curr.val < p.val) and (curr.val < q.val):
                return dfs(curr.right)
            else:
                return dfs(curr.left)
        return dfs(root)
            