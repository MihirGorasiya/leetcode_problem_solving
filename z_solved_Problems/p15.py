nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 1, 1]
answer = []

# for i in range(len(nums)):
#     for j in range(len(nums)):
#         for k in range(len(nums)):
#             if (i == j or i == k or j == k):
#                 continue
#             if (nums[i] + nums[j] + nums[k] == 0):
#                 a = [nums[i], nums[j], nums[k]]
#                 a.sort()

#                 if (a not in answer):
#                     answer.append(a)

nums.sort()

for i in range(len(nums)):
    j = i+1
    k = len(nums)-1
    while (j < k):
        print(f'{i} {j} {k}')
        if i == j or j == k or i == k:
            continue
        b = nums[i] + nums[j] + nums[k]
        if (b == 0):
            a = [nums[i], nums[j], nums[k]]
            a.sort()

            if (a not in answer):
                answer.append(a)

            j += 1
        elif b < 0:
            j += 1
        else:
            k -= 1


print(answer)
