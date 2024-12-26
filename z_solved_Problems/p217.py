nums = [1,2,3,1]
# nums = [1,2,3,4]

cNums = set()

for i in nums:
    if i in cNums:
        print(True)
    cNums.append(i)

print(False)