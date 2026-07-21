# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #input: root of a binary tree
        #output: number of good nodes in tre

        #node x is good if path from root to node x has no values > than value of node x
        #going to dfs through tree and pass largest value we find during traversal
        #contribute to global answer if curr > biggest val found

        self.answer = 0
        def dfs(curr, biggest):
            if curr == None:
                return

            if curr.val >= biggest:
                self.answer+=1
                biggest = curr.val

            dfs(curr.left, biggest)
            dfs(curr.right, biggest)

        dfs(root, root.val)
        return self.answer

        