matrix = [[1, -1], [-1, 1]]

min_count = 0
min_val = float("inf")
sum = 0
for i in matrix:
    for j in i:
        sum += abs(j)
        if j <= 0:
            min_count += 1
        min_val = min(min_val, abs(j))

if min_count % 2 != 0:
    sum -= 2 * min_val
print(sum)
