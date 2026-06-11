# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #input: binary tree
        #output: list of lists with node vals per level

        #dfs through the tree
        #track the depth

        answer = []
        def dfs(curr, depth):
            if curr is None:
                return

            if len(answer)-1 < depth:
                answer.append([curr.val])
            else:
                answer[depth].append(curr.val)

            dfs(curr.left, depth+1)
            dfs(curr.right, depth+1)

        dfs(root, 0)
        return answer

            
