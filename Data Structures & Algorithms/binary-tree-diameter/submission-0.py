# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.maxHeight(root)
        return self.diameter

        

    def maxHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        leftHeight = self.maxHeight(node.left)
        rightHeight = self.maxHeight(node.right)
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        
        return max(leftHeight, rightHeight) + 1
