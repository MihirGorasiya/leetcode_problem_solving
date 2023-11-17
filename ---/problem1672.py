accounts = [[1, 2, 3], [3, 2, 1]]
accounts = [[1,5],[7,3],[3,5]]
answer = 0

# for i in accounts:
#     sum = 0
#     for j in i:
#         sum = sum + j
#     if sum > answer:
#         answer = sum

# print(answer)

for i in accounts:
    add = sum(i)
    if add > answer:
        answer = add
    
print(answer)