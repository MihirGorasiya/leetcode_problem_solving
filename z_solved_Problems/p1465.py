h = 5
w = 4
horizontalCuts = [1, 2, 4]
verticalCuts = [1, 3]

maxDist = [0, 0]

for i in horizontalCuts:
    for j in horizontalCuts:
        print(f'{i} {j} {abs(i-j)}')

print(f'{maxDist[0]}')