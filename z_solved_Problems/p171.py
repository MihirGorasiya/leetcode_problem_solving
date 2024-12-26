columnTitle = "ZY"  # 701 -> 26 * ord(z) + ord (y)
columnTitle = "AB"
columnTitle = "FXSHRXW"
columnTitle = "AAAA"

ans = ord(columnTitle[-1]) - 64
stringLength = len(columnTitle) - 1
for i in range(stringLength):
    ans += (ord(columnTitle[i]) - 64) * pow(26, stringLength - i)
print(ans)
