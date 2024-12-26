n = 3
edges = [[0, 1], [1, 2]]

n = 4
edges = [[0, 2], [1, 3], [1, 2]]

n = 3
edges = [[0, 1]]
n = 1
edges = []

seen = {}
res = []

for i in range(n):
    seen[i] = 0
print(seen)
for edge in edges:
    seen[edge[1]] += 1

for edge in seen:
    if seen[edge] == 0:
        res.append(edge)

if len(res) == 1:
    print(res[0])
else:
    print(-1)
