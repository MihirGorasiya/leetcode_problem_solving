rowIndex = 3

# ans = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


if rowIndex == 0:
    print([[1]])
ans = [[1], [1, 1]]

for i in range(1, rowIndex):
    temp = [1]
    for j in range(0, len(ans[i]) - 1):
        temp.append(ans[i][j] + ans[i][j + 1])
    temp.append(1)
    ans.append(temp)

print(ans[-1])
    
