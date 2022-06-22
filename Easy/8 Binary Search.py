def search(nums: list[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    mid = len(nums) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        index = search(nums[:mid], target)
        return index if index != -1 else -1
    else:
        index = search(nums[mid + 1:], target)
        return mid + index + 1 if index != -1 else -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search(arr, 8.1))
