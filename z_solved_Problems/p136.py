nums = [2, 2, 1]
nums = [4, 1, 2, 1, 2]
# nums = [1]

ans = set()

i = 0
j = len(nums) - 1

while i <= j:
    
    if nums[i] in ans:
        ans.remove(nums[i])
    else:
        ans.add(nums[i])

    if i != j:
        if nums[j] in ans:
            ans.remove(nums[j])
        else:
            ans.add(nums[j])

    i += 1
    j -= 1

print(ans.pop())
