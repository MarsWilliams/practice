def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        match = seen.get(target - n)
        if match:
            return [match, i]
        seen[n] = i


print(twoSum([2, 7, 11, 15], 9))
