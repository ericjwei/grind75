def containsDuplicate(nums: list) -> bool:
    dict = {}
    for i in nums:
        if i in dict:
            return True
        else:
            dict[i] = i
    return False

nums = [1, 2, 3, 4]
print(containsDuplicate(nums))