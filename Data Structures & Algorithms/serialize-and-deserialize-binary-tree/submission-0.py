# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # gonna build tree using preorder dfs

        self.string = ""
        def dfs(curr):
            if curr == None:
                self.string+="null,"
                return

            self.string+=f'{curr.val},'
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return self.string[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # have to build tree using preorder 
        # going to just do dfs and if null, return, then increase index

        self.string = data.split(',')
        self.index = 0
        def dfs():
            if self.string[self.index] == "null":
                self.index+=1
                return
            
            node = TreeNode(int(self.string[self.index]))
            self.index+=1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

        

