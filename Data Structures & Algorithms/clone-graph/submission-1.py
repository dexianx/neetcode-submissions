"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graphClone = {}
        
        def dfs(node):
            # avoid repeating traversal when a number reference is availabl
            if node in graphClone: 
                return graphClone[node]

            copy = Node(node.val)
            graphClone[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node) if node else None