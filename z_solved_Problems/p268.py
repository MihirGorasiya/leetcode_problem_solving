nums = [3, 0, 1]
nums = [0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
l = len(nums)
ans = (l * (l + 1)) // 2

for i in nums:
    ans -= i

print(ans)
