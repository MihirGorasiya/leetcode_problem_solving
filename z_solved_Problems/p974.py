from collections import defaultdict


nums = [4, 5, 0, -2, -3, 1]
k = 5
# nums = [5]
# k = 9
# nums = [-5]
# nums = [7, 4, -10]
# k = 5

prefix_sum = 0
res = 0
prefix_count = defaultdict(int)
prefix_count[0] = 1

for n in nums:
    prefix_sum += n
    reminder = prefix_sum % k

    res += prefix_count[reminder]
    prefix_count[reminder] += 1
print(res)
