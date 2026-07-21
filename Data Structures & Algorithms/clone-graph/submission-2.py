"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #input: indirected graph
        #output: deep copy of that graph

        #going to bfs through the graph
        #append all neighbors to queue 
        #if we havent come across it before, create one and have it be value for its node pair

        if node is None:
            return

        tracker = {node:Node(node.val)} #given node : created node
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in tracker:
                    tracker[neighbor] = Node(neighbor.val)
                    queue.append(neighbor) 

                tracker[curr].neighbors.append(tracker[neighbor])
                

        return tracker[node]