n = 3
trust = [[1, 3], [2, 3], [3, 1]]
# n = 2
# trust = [[1, 2]]
# n = 3
# trust = [[1, 2], [2, 3]]
# n = 1
# trust = []


# judge = set()
# trustCount = {}
# for i in range(1, n + 1):
#     judge.add(i)
#     trustCount[i] = 0

# for trustee, trus in trust:

#     trustCount[trus]+=1
#     if trustee in judge:
#         judge.remove(trustee)
#         trustCount.pop(trustee)

# print(trustCount)
# if len(judge) == 1 and trustCount[next(iter(judge))] == n-1:
#     print(judge.pop())
# else:
#     print(-1)


judge = set(range(1,n+1))
trustCount = [0] * (n)
print(judge)
for trustee, trus in trust:
    trustCount[trus-1] += 1
    if trustee in judge:
        judge.remove(trustee)

if len(judge) == 1 and trustCount[next(iter(judge))-1] == n - 1:
    print(judge.pop())
else:
    print(-1)
