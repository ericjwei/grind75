def productExceptSelf(nums: list[int]) -> list[int]:
    res = []
    res.append(1)
    for n in nums[:-1]:
        res.append(res[-1] * n)
    post = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * post
        post *= nums[i]


