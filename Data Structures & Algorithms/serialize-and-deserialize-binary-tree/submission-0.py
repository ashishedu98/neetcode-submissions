# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = []
        def dfs(node):
            if not node:
                serial.append("null")
                return
            serial.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(serial)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        idx = 0
        def dfs():
            nonlocal nodes,idx
            if nodes[idx] =="null":
                idx+=1
                return None
            newNode = TreeNode(int(nodes[idx]))
            idx+=1
            newNode.left = dfs()
            newNode.right = dfs()
            return newNode
        return dfs()