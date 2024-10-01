# nums = [-1,2,1,-4]
# nums = [-100,-98,-2,-1]
# # nums = [0,0,0]
# target = -101
# j = 0
# k = len(nums) - 1
# ans = 1000

# for i in range(len(nums)):
#     # print(i)
#     while j <= k:
#         s = nums[i] + nums[j] + nums[k]
#         # print(f'{s} - {nums[i]} + {nums[j]} + {nums[k]}')
#         print(f'{nums[i]} + {nums[j]} + {nums[k]} \t {s} \t {target} \t {ans} \t {abs(target - ans)} \t> {abs(target - s)}')
#         if abs(target - ans) > abs(target - s):
#             # print(f'{nums[i]} + {nums[j]} + {nums[k]}')
#             ans = s

#         j += 1
#         k -= 1
#     j = i
#     k = len(nums) - i-1

# print(ans)
nums = [-1, 2, 1, -4]
i = 0
j = len(nums) - 1
while i < j + 1:
    print(f"[{nums[i]},{nums[j]}]")
    i += 1
    j -= 1
