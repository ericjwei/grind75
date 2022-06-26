from __future__ import annotations

class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def valid(node: TreeNode, left: int, right: int):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False
        
        return (valid(node.left, left, node.val) and 
            valid(node.right, node.val, right))
    return valid(root, float("-inf"), float("inf"))