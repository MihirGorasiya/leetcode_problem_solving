from collections import defaultdict


nums = [1, 2, 1,2,1]
k = 3

prefix_count = defaultdict(int)
prefix_count[0]=1 
prefix_sum = 0
res = 0

for n in nums:
    prefix_sum += n
    diff = prefix_sum-k

    res += prefix_count[diff]
    prefix_count[prefix_sum] += 1
print(res)
