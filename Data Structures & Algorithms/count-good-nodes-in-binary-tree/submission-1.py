# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxfar):
            if not node:
                return 0
            
            if node.val >= maxfar:
                res = 1
            else:
                res = 0

            maxfar = max(maxfar, node.val)
            res += dfs(node.left, maxfar)
            res += dfs(node.right, maxfar)
            return res
        
        return dfs(root, root.val)


                
