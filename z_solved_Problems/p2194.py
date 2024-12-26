s = "K1:L2"

c1 = ord(s[0])
c2 = ord(s[3])
r1 = ord(s[1])
r2 = ord(s[4])
res = []
for i in range(c1, c2 + 1):
    for j in range(r1, r2 + 1):
        res.append(f"{chr(i)}{chr(j)}")

print(res)