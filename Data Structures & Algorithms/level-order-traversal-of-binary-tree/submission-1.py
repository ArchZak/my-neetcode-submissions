# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        given root of binary tree
        return level order traversal as nested lists
        each sublist is values of nodes at level from left to right

        can have an empy tree

        approaches:

        bfs
            going to bfs
            when going through level gonna add it to sublist
            gonna create a new list when done with curr part of queue 

        literal:
            while queue get curr node
            we can build a queue within the queue 
            we know whatever is in the curr queue is the curr level
        """
        if not root:
            return []
        queue = deque([deque([root])])
        answer = []
        while queue:
            level_queue = queue.popleft()
            neighbors = deque()
            sublist = []
            while level_queue:
                curr = level_queue.popleft()
                sublist.append(curr.val)
                if curr.left:
                    neighbors.append(curr.left)
                if curr.right:
                    neighbors.append(curr.right)
            answer.append(sublist)
            if neighbors:
                queue.append(deque(neighbors))
        
        return answer
        