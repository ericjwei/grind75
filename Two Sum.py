class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hashmap:
                return [i, hashmap[pair]]
            hashmap[nums[i]] = i

nums = [3,2,4]
s = Solution
print(s.twoSum2(s, nums, 5))
