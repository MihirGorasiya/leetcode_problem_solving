nums = [4, 3, 1, 6]
queries = [[0, 2], [2, 3]]

# # nu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
# nums = [4, 3, 1, 6, 5, 7, 6, 2, 4, 5, 6, 7, 8, 9, 9, 1]
# # pa = [1, 2, 1, 2, 3, 1, 2, 1, 1, 2, 3, 4, 5, 6, 1, 1]
# queries = [[8, 13], [0, 2], [2, 3], [9, 10], [9, 12]]

# nums = [3,4,1,2,6]
# queries = [[0,4]]
nums = [1, 1]
queries = [[0, 1]]

parity_len = [1]
previous = nums[0] % 2
for i in range(1, len(nums)):
    if previous != nums[i] % 2:
        parity_len.append(parity_len[-1] + 1)
    else:
        parity_len.append(1)
    previous = nums[i] % 2
res = []
for first, last in queries:
    if (last - parity_len[last]) <= first:
        res.append(True)
    else:
        res.append(False)

print(parity_len)
print(res)
