box = [["#", ".", "#"]]
box = [["#", ".", "*", "."], ["#", "#", "*", "."]]
box = [
    ["#", "#", "*", ".", "*", "."],
    ["#", "#", "#", "*", ".", "."],
    ["#", "#", "#", ".", "#", "."],
]

resultBox = [[] for _ in range(len(box[0]))]

for i in range(len(box) - 1, -1, -1):
    k = len(resultBox) - 1
    for j in range(len(box[i]) - 1, -1, -1):
        if box[i][j] == ".":
            resultBox[j].append(box[i][j])
        elif box[i][j] == "*":
            resultBox[j].append(box[i][j])
            k = j - 1
        else:
            resultBox[j].append(".")
            resultBox[k][len(box) - 1 - i] = "#"
            k -= 1

print(resultBox)
