nums = [1, 5, 4, 2, 9, 9, 9]
nums = [4, 4, 4]
nums = [1, 1, 1, 7, 8, 9]
nums = [9, 9, 9, 1, 2, 3]
nums = [1, 2, 2]
k = 2

seen = {}
subSet = {}
res = 0
subSetSum = 0

i = 0
j = len(nums)

while i < j:

    if subSet.get(nums[i]) == None:
        subSet[nums[i]] = 1
    else:
        subSet[nums[i]] += 1

    subSetSum += nums[i]

    if i < k:
        if len(subSet) == k and subSetSum > res:
            res = subSetSum
        i += 1
        continue

    if subSet.get(nums[i - k]) == None or subSet[nums[i - k]] == 1:
        subSet.pop(nums[i - k])
    else:
        subSet[nums[i - k]] -= 1

    subSetSum -= nums[i - k]

    if len(subSet) == k and subSetSum > res:
        res = subSetSum

    print(f"{len(subSet)} - {subSet}")
    i += 1
print(res)
# while i < j:
#     # if i < k:
#     #     subSet.add(nums[i])
#     #     subSetSum += nums[i] if nums[i] not in subSet else 0
#     print(f'{i} -> {nums[i]}')
#     if i>=k:
#         if seen.get(nums[i - k]) == None:
#             subSet.remove(nums[i - k])
#         elif seen.get(nums[i - k]) == 1:
#             seen.pop(nums[i - k])
#         else:
#             seen[nums[i - k]] = seen[nums[i - k]] - 1

#     if nums[i] in subSet:
#         if seen.get(nums[i]) != None:
#             seen[nums[i]] = seen[nums[i]] + 1
#         else:
#             seen[nums[i]] = 1
#         i += 1
#         continue
#     else:
#         subSet.add(nums[i])

#     print(
#         f"first value: {nums[i-k]} | Last Value: {nums[i]} |seen: {seen} | subset: {subSet}"
#     )
#     # print(f"seen: {seen} | subset: {subSet}")
#     i += 1

# print(subSetSum)
