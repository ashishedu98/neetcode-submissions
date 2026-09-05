# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(node,left,right):
            if not node:
                return True
            if left is not None and node.val <= left:
                return False 
            if right is not None and node.val >= right:
                return False
            return bst(node.left,left,node.val) and bst(node.right,node.val,right)  

        return bst(root,None,None)
            