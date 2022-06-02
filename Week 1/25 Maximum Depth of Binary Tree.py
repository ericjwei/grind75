from __future__ import annotations
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left = maxDepth(root.left) + 1
    right = maxDepth(root.right) + 1
    return max(left, right)

def buildTree(arr: list, i: int, root: TreeNode) -> TreeNode:
    if i >= len(arr) or not arr[i]:
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2 * i + 1, root)
    root.right = buildTree(arr, 2 * i + 2, root)     
    return root

def printTree(root: TreeNode) -> None:
    if not root:
        return
    printTree(root.left)
    print(root.val, end = " ")
    printTree(root.right)


# arr = [3,9,20,None,None,15,7]
arr = [1, None, 2]
root = TreeNode()
root = buildTree(arr, 0, root)
# printTree(root)
print(maxDepth(root))