"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #input: node of undirected, connected graph
        #output: return deep copy of ^^

        #graph in test case is adj list
        #nodes are numbered 1-n where each index is same as adj list val and is 1-index
        #input node is always first node (so has value of 1)

        #constraints: 
        #can just have an empty node, but will max out at 100 nodes
        #graph is connected so we're fine there
        #no duplicate edges or self loops

        #dfs
        #track visited nodes, if visited then we return
        #if not, add it to visited set
        #then kick dfs off on all the neighbors

        #bfs
        #track visited nodes, if visited then skip
        #append neighbors to queue if havent seen

        from collections import deque

        if not node:
            return None

        queue = deque([node])
        tracker = {node: Node(node.val)}

        while queue:
            curr = queue.popleft()

            for n in curr.neighbors:
                if n not in tracker:
                    queue.append(n)
                    tracker[n] = Node(n.val)
                tracker[curr].neighbors.append(tracker[n])
        
        return tracker[node]
