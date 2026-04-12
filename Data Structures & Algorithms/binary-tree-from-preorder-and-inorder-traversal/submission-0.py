# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root_value = preorder[0]
        root = TreeNode(root_value)

        for i in range(len(inorder)):
            if inorder[i] == root_value:
                root_index = i
                break
        left_inorder = inorder[0: root_index]
        right_inorder = inorder[root_index + 1: ]

        nodes_len = len(left_inorder)
        
        left_preorder = preorder[1 : 1 + nodes_len]
        right_preorder = preorder[nodes_len + 1 : ]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

            