nums = [8, 1, 2, 2, 3]
nums = [6,5,4,8]
answer = []

sortedNums = nums.copy()
sortedNums.sort()

for i in nums:
    answer.append(sortedNums.index(i))

print(answer)
