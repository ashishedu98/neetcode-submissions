"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeMap = {}
        nodeMap[node] = Node(node.val)
        q = deque([node])
        while q:
            curr = q.popleft()
            for x in curr.neighbors:
                if x not in nodeMap:
                    nodeMap[x] = Node(x.val)
                    q.append(x)
                nodeMap[curr].neighbors.append(nodeMap[x])
        return nodeMap[node]