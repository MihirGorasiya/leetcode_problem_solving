import math
# nums1 = [1, 3]
# nums2 = [2]

nums1 = [1, 2]
nums2 = [3]

nums3 = nums1 + nums2
nums3.sort()

# TODO: solve using if condition

# if (len(nums3) % 2 == 0):
#     i = math.floor(len(nums3)/2)-1
#     print((nums3[int(i)] + nums3[int(i+1)])/2)
# else:
#     i = ((len(nums3))-1)/2
#     print(nums3[int(i)])


i = 0
j = len(nums3)-1


while (i < j):
    i = i+1
    j = j-1
else:
    print((nums3[i]+nums3[j])/2)
