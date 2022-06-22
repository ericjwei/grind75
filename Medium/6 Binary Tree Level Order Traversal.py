from __future__ import annotations
import collections

class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: list[TreeNode]) -> list[list[int]]:
    res = []

    q = collections.deque[TreeNode]()
    q.append(root)

    while q:
        qLen = len(q)
        level = []
        for _ in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res
