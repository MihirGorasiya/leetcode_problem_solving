jewels = "aA"
stones = "aAAbbbb"


count = 0
jews = {}
for i in jewels:
    jews[i] = 1

for i in stones:
    if i in jews:
        count += 1

print(count)
