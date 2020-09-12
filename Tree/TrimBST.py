# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def helper(node, parent, L, R):
            if node is None:
                return 
            if parent:
                if node is None:
                    return
                if node.val >= L and node.val <= R:
                    helper(node.left, node, L, R)
                    helper(node.right, node, L, R)
                else:
                    if node.val < L:
                        node.left = None
                        parent.left = node.right
                        helper(node.right, parent, L, R)
                    elif node.val > R:
                        node.right = None
                        parent.right = node.left
                        helper(node.left, parent, L, R)
            else:
                nonlocal root
                if node.val < L:
                    root = node.right
                    helper(root, None, L, R)
                elif node.val > R:
                    root = node.left
                    helper(root, None, L, R)
                else:
                    helper(node.left, node, L, R)
                    helper(node.right, node, L, R)
        helper(root, None, L, R)
        return root
