from tkinter.tix import Tree


class TreeNode:
    def __init__(self, x: int, right: int | None = None, left: int | None = None):
        self.val = x
        self.left = left
        self.right = right

# All node values are unique
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return
    if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
        return root
    elif root.val > p.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return lowestCommonAncestor(root.right, p, q)
    
def buildTree(arr: list, i) -> TreeNode:
    if i >= len(arr) or arr[i] == None:
        return
    
    node = TreeNode(arr[i])
    node.left = buildTree(arr, i * 2 + 1)  
    node.right = buildTree(arr, i * 2 + 2)
    return node

def printTree(root: TreeNode, i) -> None:
    if root != None:
        printTree(root.left, i - 1)
        print(root.val, end = " " * i)
        printTree(root.right, i - 1)

arr = [6,2,8,0,4,7,9,None,None,3,5]
root = buildTree(arr, 0)
printTree(root, len(arr) // 2)
print(lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val)