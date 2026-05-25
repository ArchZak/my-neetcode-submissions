# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #input: root of a binary tree and an int of which node to delete
        #output: delete new tree

        #need to actually find the node we want to delete by traversing down
        #once found, node can either have 0,1,2 children
        #if no left child, replace with right
        #if no right child, replace with left
        #if both children, go to right, and go all the way down left
        #once at the bottom of it, copy the value to node to replace and delete old one 
        
        #basically just want to force a situation where you delete leaf node by
        #starting the process over again with right subtree and val we copied upward

        if root is None:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)
        
        return root
