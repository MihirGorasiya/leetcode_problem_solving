nums = [4, 6, 1, 2]
k = 2

nums = [1, 1, 1, 1]
k = 10

# nums = [52,34]
# k = 21
nums = [49, 26]
k = 12

nums.sort()

res = 0
l = 0

for r in range(len(nums)):
    while nums[r] - nums[l] > 2 * k:
        l += 1

    res = max(res, r - l + 1)
print(res)
