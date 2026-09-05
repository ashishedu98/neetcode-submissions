# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque() 
        if root:
            q.append([root])
            res=[[root.val]]
        else:
            return []
        while q:
            lis = q.popleft()
            temp=[]
            tempres=[]
            for x in lis:
                if x.left:
                    temp.append(x.left)
                    tempres.append(x.left.val)
                if x.right:
                    temp.append(x.right)
                    tempres.append(x.right.val)
            if temp:
                q.append(temp)
                res.append(tempres)
        return res
        