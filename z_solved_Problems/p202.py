n = 19
seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(digit) ** 2 for digit in str(n))

print(n == 1)
