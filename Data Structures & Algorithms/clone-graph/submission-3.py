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
        #going to dfs through the graph and track nodes we visited and rebuild the graph

        #just dfs through graph normally

        visited = set()
        tracker = {}
        numbers = []

        def dfs(curr):
            if curr in visited:
                return
            if curr == None:
                tracker[curr] = None
                return
            numbers.append(curr.val)
            visited.add(curr)

            if curr not in tracker:
                tracker[curr] = Node(curr.val, [])
                
            for neighbor in curr.neighbors:
                if neighbor not in tracker:
                    tracker[neighbor] = Node(neighbor.val)
                tracker[curr].neighbors.append(tracker[neighbor])
                dfs(neighbor)

        dfs(node)
        return tracker[node]
