# nums = [3, 2, 2, 3]
# val = 3
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
# i = 0
# length = len(nums)
# while i < len(nums):
#     if nums[i] == val:
#         nums.remove(val)
#         length -= 1
#     else:
#         i += 1

# print(length)
# print(nums)

j = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[j] = nums[i]
        j+=1
    
print(j)