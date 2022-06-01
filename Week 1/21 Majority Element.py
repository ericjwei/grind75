def majorityElement(nums: list[int]) -> int:
    majority = nums[0]
    count = 0
    for i in nums:
        if i == majority:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority = i
            count = 1
    return majority

nums = [2,2,3,4,1,1,1,2,2,2]
print(majorityElement(nums))