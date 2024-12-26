nums = [3, 2, 1]
# nums = [1, 2]
# nums = [2, 2, 3, 1]
# nums = [5, 2, 2]

max1 = max2 = max3 = float("-inf")

for i in nums:
    if i > max1:
        max3 = max2
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max3 = max2
        max2 = i
    elif i > max3 and i != max2 and i != max1:
        max3 = i

if max3 == float("-inf"):
    print(max1)
else:
    print(max3)
