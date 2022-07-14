from heapq import heapify, heappop

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    minHeap = []
    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])
    
    heapify(minHeap)
    res = []
    while k > 0:
        dist, x, y = heappop(minHeap)
        res.append([x, y])
        k -= 1

    return res

points = [[1, 3], [-2, 2]]
k = 1
print(kClosest(points, k))