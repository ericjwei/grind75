def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
            
        l, r = i + 1, len(nums) - 1
        while l < r:
            threesome = a + nums[l] + nums[r]
            if threesome > 0:
                r -= 1
            elif threesome < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

nums = [-1,0,0,1,2,-1,-4]
print(threeSum(nums))