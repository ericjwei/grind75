from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
    if not grid:
        return -1
    
    freshCount = 0
    rows, cols = len(grid), len(grid[0])
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                freshCount += 1
    
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    time = 0
    l = len(q)
    while q:
        while l > 0:
            row, col = q.popleft()
            l -= 1
            for dr, dc in directions:
                row, col = row + dr, col + dc
                if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                    freshCount -= 1
                    grid[row][col] = 2
                    q.append((row, col))
        time += 1
        l = len(q)

    if freshCount > 0:
        return -1
    else: 
        return time





    