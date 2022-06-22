from operator import invert


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

def buildTree(root: TreeNode, arr: list, i: int, n: int) -> TreeNode:
    if i < n:
        root = TreeNode(arr[i])
        root.left = buildTree(root.left, arr, i * 2 + 1, n)
        root.right = buildTree(root.right, arr, i * 2 + 2, n)

    return root

def printTree(root: TreeNode) -> None:
    if root != None:
        printTree(root.left)
        print(root.val, end = " ")
        printTree(root.right)

arr = [4, 2, 7, 1, 3, 6, 9]
root = None
root = buildTree(root, arr, 0, len(arr))
root = invertTree(root)
printTree(root)
