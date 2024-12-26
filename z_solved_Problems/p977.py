nums = [-4, -1, 0, 3, 10]

ans = []
l = 0
r = len(nums) - 1

while l <= r:
    if abs(nums[l]) < abs(nums[r]):
        ans.append(nums[r] ** 2)
        r -= 1
    else:
        ans.append(nums[l] ** 2)
        l += 1
print(ans)
l = 0
r = len(ans) - 1
while l < r:
    ans[l], ans[r] = ans[r], ans[l]
    l += 1
    r -= 1

print(ans)