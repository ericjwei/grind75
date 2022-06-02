def meetingRooms(intervals: list[list[int]]) -> bool:
    intervals = quickSortInterval(intervals)
    for i in range(1,len(intervals)):
        if intervals[i - 1][1] > intervals[i][0]:
            return False
    return True

def quickSortInterval(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) <= 1:
        return intervals
    left = quickSortInterval(intervals[:len(intervals) // 2])
    right = quickSortInterval(intervals[len(intervals) // 2:])
    return sort(left, right)

def sort(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i][0] < b[j][0]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result

a = [[1, 2], [5, 6], [3, 4], [6, 8], [0, 1]]
print(meetingRooms(a))

def meetingRoomsConcise(intervals: list[list[int]]) -> bool:
    intervals = sorted(intervals, key = lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True

print(meetingRoomsConcise(a))