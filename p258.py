num = 40
numStr = str(num)
ans = 0

while len(numStr) > 1:
    ans = 0
    for i in numStr:
        ans += int(i)
    numStr = str(ans)

print(ans)