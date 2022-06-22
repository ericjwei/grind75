from __future__ import annotations

class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] = []):
        self.val = val
        self.neighbors = neighbors

def cloneGraph(node: Node) -> Node:
    oldToNew = {}

    def dfs(node: Node):
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    
    return dfs(node) if node else None
    