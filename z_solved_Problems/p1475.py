prices = [8, 4, 6, 2, 3]

res = [p for p in prices]

stack = []


for i in range(len(prices)):

    while stack and prices[stack[-1]] > prices[i]:
        j = stack.pop()
        res[j] -= prices[i]

    stack.append(i)


print(res)
