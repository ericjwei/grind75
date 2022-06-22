class TreeNode:
    def __init__(self, val: int = 0, left: int | None = None, right: int | None = None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:
    return isBalancedHelper(root)[1]
    
def isBalancedHelper(root: TreeNode, balanced: bool = True) -> tuple[int, bool]:
    if not (root and balanced):
        return 0, balanced  
    
    lh, balanced = isBalancedHelper(root.left, balanced)
    rh, balanced = isBalancedHelper(root.right, balanced)

    if abs(lh - rh) > 1:
        balanced = False

    return max(lh, rh) + 1, balanced

def buildTree(arr: list, i: int) -> TreeNode:
    if i >= len(arr) or not arr[i]:
        return
    root = TreeNode(arr[i])
    root.left = buildTree(arr, i * 2 + 1)
    root.right = buildTree(arr, i * 2 + 2)
    return root

arr = [1,2,2,3,3,None,None,4,4]
root = buildTree(arr, 0)
print(isBalanced(root))