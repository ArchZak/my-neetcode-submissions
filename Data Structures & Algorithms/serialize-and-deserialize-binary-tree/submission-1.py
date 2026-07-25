# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder op
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
        self.split_data = data.split(",")
        # build tree via preorder
        self.i = 0
        def dfs():
            if self.split_data[self.i] == 'null':
                self.i+=1
                return

            curr = TreeNode(int(self.split_data[self.i]))
            self.i+=1
            curr.left = dfs()
            curr.right = dfs()
            return curr

        return dfs()


            

            



            



