code = [5, 7, 1, 4]
k = 3
# code = [2, 4, 9, 3]
# k = -2
# code = [1,2,3,4]
# k = 0

length = len(code)

if k == 0:
    print([0] * length)
    
res = []
last = k
sum = 0

for i in range(1, k + 1) if k > 0 else range(k, 0):
    sum += code[i]
res.append(sum)

for i in range(1, length):
    if k > 0:
        sum -= code[i]
        last = last + 1 if last < length - 1 else 0
        sum += code[last]
    else:
        sum -= code[last]
        last = last + 1
        sum += code[i - 1]
    res.append(sum)

print(res)
