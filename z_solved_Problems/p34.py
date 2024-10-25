nums = [5, 7, 7, 8, 8, 10]
target = 8
# nums = [5, 7, 7, 8, 8, 10]
# target = 6
# nums = [2, 2]
# target = 2
# nums = [1]
# target = 1
nums = [1, 3]
target = 1
nums = [2, 2]
target = 3

first = 0
last = len(nums) - 1
res = [-1, -1]
while first <= last:
    mid = (first + last) // 2

    print(f"{first} + {last} = {mid}")
    if target == nums[mid]:
        # first = last = mid
        # while first - 1 >= 0 and nums[first - 1] == target:
        #     first -= 1
        # while last + 1 <= len(nums) - 1 and nums[last + 1] == target:
        #     last += 1
        # res[0] = first
        # res[1] = last

        break

    elif target > nums[mid]:
        first = mid + 1
    else:
        last = mid - 1


print(res)
