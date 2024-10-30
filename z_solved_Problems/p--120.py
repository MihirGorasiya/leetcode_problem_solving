# triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
# triangle = [[-10]]
triangle = [[-1], [2, 3], [1, -1, -3]]

minPath = 0
curIndex = 0
pathSteps = []
i = len(triangle) - 1
while i >= 0:

    pathSteps.append(min(triangle[i]))
    i -= 1

print(sum(pathSteps))
