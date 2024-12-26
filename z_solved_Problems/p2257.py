# m = 4
# n = 6
# guards = [[0, 0], [1, 1], [2, 3]]
# walls = [[0, 1], [2, 2], [1, 4]]
m = 2
n = 7
guards = [[1, 5], [1, 1], [1, 6], [0, 2]]
walls = [[0, 6], [0, 3], [0, 5]]

matrix = [[0 for i in range(n)] for j in range(m)]
res = m * n
# print(res)

for guard in guards:
    matrix[guard[0]][guard[1]] = 1
    res -= 1

for wall in walls:
    matrix[wall[0]][wall[1]] = 2
    res -= 1

print(matrix)
print(res)

for guard in guards:
    i = guard[0] - 1
    j = guard[1]

    while i >= 0:
        if matrix[i][j] == 2:
            break
        if matrix[i][j] != 3 and matrix[i][j] == 0:
            matrix[i][j] = 3
            res -= 1

        # print(f"matrix[{i}][{j}] = {matrix[i][j]}")
        i -= 1

    i = guard[0] + 1

    while i < m:
        if matrix[i][j] == 2:
            break
        if matrix[i][j] != 3 and matrix[i][j] == 0:
            matrix[i][j] = 3
            res -= 1
        # print(f"matrix[{i}][{j}] = {matrix[i][j]}")
        i += 1
    print()

    i = guard[0]
    j = guard[1] - 1
    while j >= 0:
        if matrix[i][j] == 2:
            break
        if matrix[i][j] != 3 and matrix[i][j] == 0:
            matrix[i][j] = 3
            res -= 1
        j -= 1

    j = guard[1] + 1
    while j < n:
        if matrix[i][j] == 2:
            break
        if matrix[i][j] != 3 and matrix[i][j] == 0:
            matrix[i][j] = 3
            res -= 1
        j += 1

    print(f"Guard: {guard} | res = {res}")
    print(matrix)

# for row in range(m):
#     for column in range(n):
#         if matrix[row][column] == 0:
#             res += 1
print(matrix)
print(res)

[0, 0, 1, 2, 0, 2, 2]
[0, 1, 0, 0, 0, 1, 1]

"""
m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]

matrix = [[0 for i in range(n)] for j in range(m)]

res = m * n

for guard in guards:
    matrix[guard[0]][guard[1]] = 1
    res -= 1

for wall in walls:
    matrix[wall[0]][wall[1]] = 2
    res -= 1


for guard in guards:
    i = guard[0] - 1
    j = guard[1]

    while i >= 0:
        if matrix[i][j] == 2:
            break
        # matrix[i][j] = 3
        res -= 1
        i -= 1

    i = guard[0] + 1

    while i < m:
        if matrix[i][j] == 2:
            break
        # matrix[i][j] = 3
        res -= 1
        i += 1
    print()

    i = guard[0]
    j = guard[1] - 1
    while j >= 0:
        if matrix[i][j] == 2:
            break
        # matrix[i][j] = 3
        res -= 1
        j -= 1

    j = guard[1] + 1
    while j < n:
        if matrix[i][j] == 2:
            break
        # matrix[i][j] = 3
        res -= 1
        j += 1


print(res)
"""
