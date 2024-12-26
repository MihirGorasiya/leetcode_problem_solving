arr = [10, 2, 5, 3]
arr = [7, 1, 14, 11]
# arr = [3, 1, 7, 11]
# arr = [-10, 12, -20, -8, 15]
seen = set()

for num in arr:
    if num / 2 in seen or num * 2 in seen:
        print(True)

    seen.add(num)

print(False)
