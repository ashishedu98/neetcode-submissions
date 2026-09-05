# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree=[]
        subTree=[]
        def dfs(node, op):
            if not node:
                op.append("null")
                return
            op.append(str(node.val))
            dfs(node.left, op)
            dfs(node.right, op)
            return 
        
        dfs(root, tree)
        dfs(subRoot, subTree)
        return ",".join(subTree) in ",".join(tree)

# class Solution:   
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

#         def sametree(p, q):

#             if not p and not q:
#                 return True
            
#             if not p or not q or p.val != q.val:
#                 return False

#             return (sametree(p.left, q.left) and sametree(p.right, q.right))

#         if not root:
#             return  False

#         if sametree(root, subRoot):
#             return True

#         return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) 
 