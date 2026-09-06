# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preOrderId = inOrderId = 0
        def dfs(limit):
            nonlocal preOrderId, inOrderId
            if preOrderId >= len(preorder):
                return None
            if inorder[inOrderId] == limit:
                inOrderId += 1
                return None
            root = TreeNode(preorder[preOrderId])
            preOrderId += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))