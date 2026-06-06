"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        #input: a graph
        #output: the same graph but rebuilt

        #bfs through the graph and rebuild the nodes that way
        #start with a queue and tracking with curr node in
        #pop from the left and then loop through its neighbors
        #create the key:value is needed, then add it to neighbor list

        if node is None:
            return 

        tracking = {node:Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for n in curr.neighbors:
                if n not in tracking:
                    tracking[n] = Node(n.val)
                    queue.append(n)

                tracking[curr].neighbors.append(tracking[n])

        return tracking[node]
