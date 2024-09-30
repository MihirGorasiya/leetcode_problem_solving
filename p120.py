# triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
# triangle = [[-10]]
triangle = [[-1], [2, 3], [1, -1, -3]]
minPath = 0
curIndex = 0

for i in triangle:
    print(i)
    if len(i) > curIndex + 1:
        minimum = min(i[curIndex], i[curIndex + 1])
        print(minimum)
        curIndex = i.index(minimum)
        minPath += minimum
    else:
        minimum = i[curIndex]
        print(minimum)
        minPath += i[curIndex]
        
        
print(minPath)
