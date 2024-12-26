matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

j = len(matrix)
for i in range(j):
    for k in range(i):
        matrix[i][k], matrix[k][i] = matrix[k][i], matrix[i][k]


i = 0
j = len(matrix) - 1
while i < j:
    for k in range(len(matrix)):
        matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]

    i += 1
    j -= 1

print(matrix)