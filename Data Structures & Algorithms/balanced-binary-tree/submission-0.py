# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.height(root) != -1

    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        leftH = self.height(node.left)
        rightH = self.height(node.right)

        if leftH == -1:
            return -1
        if rightH == -1:
            return -1
        if abs(leftH - rightH) > 1:
            return -1
        return 1 + max(leftH, rightH)