nums = [-1, 2, 1, -4]
target = 1
nums.sort()
res = float("inf")
length = len(nums)

for i in range(length - 2):
    left = i + 1
    right = length - 1
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum == target:
            print(f"answer: {sum}")
        elif sum < target:
            left += 1
        else:
            right -= 1
        if abs(sum-target) < abs(res - target):
            res = sum

print(res)