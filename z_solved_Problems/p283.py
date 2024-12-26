nums = [0, 1, 0, 3, 12]
nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]

i = 0
j = 1

while j < len(nums) and i < len(nums):
    if nums[i] != 0:
        print(f"{nums} | {i} | {j} 2")
        i += 1
        j = i + 1
        continue

    if nums[j] == 0:
        print(f"{nums} | {i} | {j} 1")
        j += 1
        continue

    # if nums[i] != 0 and nums[j] != 0:
    #     print(f"{nums} | {i} | {j} 0")
    #     i += 1
    #     j += 1
    #     continue

    if nums[i] == 0 and nums[j] != 0:
        print(f"{nums} | {i} | {j} 3")
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j += 1

print(nums)
