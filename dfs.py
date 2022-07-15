from __future__ import annotations

class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root: TreeNode):
    if root:
        dfs(root.left)
        print(root.val)
        dfs(root.right)

    