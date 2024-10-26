matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

rows = set()
columns = set()


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            rows.add(i)
            columns.add(j)

for i in range(len(matrix)):
    if i in rows:
        matrix[i] = [0] * (len(matrix[i]))
        continue
    for j in range(len(matrix[i])):
        if j in columns:
            matrix[i][j] = 0


print(matrix)
