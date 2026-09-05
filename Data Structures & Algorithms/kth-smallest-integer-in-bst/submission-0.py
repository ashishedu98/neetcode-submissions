# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = root.val
        nth = k
        def dfs(node):
            nonlocal smallest, nth
            if not node:
                return
            dfs(node.left)
            if nth == 0:
                return
            nth-=1
            if nth == 0:
                smallest = node.val
                return
            dfs(node.right)

        dfs(root)
        return smallest