nums = [1, 2, 2, 4]
nums = [3, 2, 2]

numSet = set(nums)
ans = []
length = len(nums)
total = (length * (length + 1)) // 2
totalNums = sum(nums)
totalNumSet = sum(numSet)

ans.append(totalNums - totalNumSet)
ans.append(total - totalNumSet)

print(ans)