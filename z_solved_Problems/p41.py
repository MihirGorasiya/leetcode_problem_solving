nums = [1, 2, 0]
# nums = [100000, 3, 4000, 2, 15, 1, 99999]
nums = [2, 2]

seen = set()
res = 1
for n in nums:
    print(f"{n} == {res} == {res == n} | {seen}")
    if n == res:
        res += 1
    else:
        seen.add(n)

for i in range(len(seen)):
    if res in seen:
        res += 1


print(res)
