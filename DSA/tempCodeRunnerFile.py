a = [0, 1, 2, 0, 1, 2]

low = 0
mid = 0
high = len(a)-1
print(a[high])

while mid <= high:
    if a[mid] == 0:
        a[low],  a[mid] = a[mid], a[low]
        low += 1
        mid += 1
    elif a[mid] == 2:
        a[mid], a[high] = a[high], a[mid]
        high -= 1
    else:
        mid += 1

print(a)
