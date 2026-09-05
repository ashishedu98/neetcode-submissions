# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # pPath=[]
        # qPath=[]
        # def dfs(node, op, target):
        #     if node is None:
        #         return 
        #     op.append(node)
        #     if node.val == target.val:
        #         return
        #     if node.val>target.val:
        #         dfs(node.left, op,target)
        #     else:
        #         dfs(node.right, op,target)
        #     return
        # dfs(root,pPath,p)
        # dfs(root,qPath,q)
        # i=0
        # while i < len(pPath) and i < len(qPath) and pPath[i] == qPath[i]:
        #     i += 1

        # return pPath[i - 1]

        while root:
            if p.val<root.val and q.val<root.val:
                root = root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root