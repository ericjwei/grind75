def maxSubArray(nums: list[int]) -> int:
    maximum = nums[0]
    curr = 0

    for num in nums:
        curr = max(curr + num, num)
        maximum = max(curr, maximum)

    return maximum

def maxSubArraySelection(nums: list[int]) -> list[int]:
    maximum = localMax = nums[0]
    maxArray = []
    i = 0
    j = 1

    while j < len(nums):
        if localMax + nums[j] < nums[j]:
            i = j
            localMax = nums[j]
        else:
            localMax += nums[j]
        j += 1
        if localMax > maximum:
            maximum = localMax
            maxArray = nums[i:j]

    return maxArray

ll = [-2,1,-3,4,-1,2,1,-5,4,-10,7]
s = maxSubArraySelection(ll)
print(*s)
