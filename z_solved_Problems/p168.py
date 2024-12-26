columnNumber = 2147483647
columnNumber = 28
columnNumber = 18279
ans = ""
while columnNumber > 0:
    offset = (columnNumber - 1) % 26
    ans += chr(ord("A") + offset)
    columnNumber = (columnNumber-1) // 26
print(ans[::-1])
