"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #dfs
        #need visited + tracker to map old to new
        
        #check if we visited node, if so return
        #append it to visited if not
        #then iterate through neighbors and dfs em

        #bfs
        #need queue + tracker that's it

        #while we have a queue
        #pop node and then add neighbors to queue if we havent visited

        from collections import deque

        if node == None:
            return None

        tracker, queue = {node: Node(node.val)}, deque([node])

        while queue:
            curr = queue.popleft()

            for n in curr.neighbors:
                if n not in tracker:
                    tracker[n] = Node(n.val)
                    queue.append(n)
                tracker[curr].neighbors.append(tracker[n])

        return tracker[node]


