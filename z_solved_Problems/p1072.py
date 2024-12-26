matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]

seen = {}

for row in matrix:
    if row[0] == 0:
        arrToString = "".join(str(x) for x in row)
        if seen.get(arrToString) != None:
            seen[arrToString] += 1
        else:
            seen[arrToString] = 1
    else:
        arrToString = "".join(str(int(not x)) for x in row)
        if seen.get(arrToString) != None:
            seen[arrToString] += 1
        else:
            seen[arrToString] = 1

print(max(seen.values()))
