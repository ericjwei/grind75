from __future__ import annotations
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

diameter = 0
def diameterOfBinaryTree(root: TreeNode) -> int:
    if not root:
        return -1
    
    left = diameterOfBinaryTree(root.left)
    right = diameterOfBinaryTree(root.right)
    diameter = max(diameter, left + right + 2)
    return max(left, right) + 1
