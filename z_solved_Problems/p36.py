board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", ".", "6", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

# board = [
#     [".", ".", "4", ".", ".", ".", "6", "3", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["5", ".", ".", ".", ".", ".", ".", "9", "."],
#     [".", ".", ".", "5", "6", ".", ".", ".", "."],
#     ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
#     [".", ".", ".", "7", ".", ".", ".", ".", "."],
#     [".", ".", ".", "5", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
# ]
res = True
i = 0
j = 0

rows = set()
square1 = set()
square2 = set()
square3 = set()

while i < 9:
    while j < 9:
        if board[i][j] == ".":
            j += 1
            continue
        if board[i][j] in rows:
            res = False
        else:
            rows.add(board[i][j])

        if j < 3:
            if board[i][j] in square1:
                res = False
            else:
                square1.add(board[i][j])
        elif j < 6:
            if board[i][j] in square2:
                res = False
            else:
                square2.add(board[i][j])
        else:
            if board[i][j] in square3:
                res = False
            else:
                square3.add(board[i][j])

        j += 1
    rows = set()
    j = 0
    i += 1

    if i % 3 == 0:
        square1 = set()
        square2 = set()
        square3 = set()

i = 0
j = 0
while i < 9:
    while j < 9:
        if board[j][i] == ".":
            j += 1
            continue        
        if board[j][i] in rows:
            res = False
        else:
            rows.add(board[j][i])
        j += 1
    j = 0
    rows = set()

    i += 1

print(res)
