a = [1, 2, 3]
b = [1, 2, 3, 4]

# ------------------------- Reverse Array -------------------------
# with looping
'''

def reverseArray(array):
    s = 0
    e = len(array)-1
    while s < e:
        array[s], array[e] = array[e], array[s]
        s += 1
        e -= 1

# recursive function


def reverseArr(a, s, e):
    if (s >= e):
        return
    a[s], a[e] = a[e], a[s]
    reverseArr(a, s+1, e-1)


print(a)
print(b)
reverseArr(a, 0, 2)
reverseArr(b, 0, 3)
print(a)
print(b)
'''
# ------------------------- Rotate Array -------------------------


def rotateArray(a):
    aLength = len(a)
    last = a[aLength-1]

    for i in range(aLength-1, 0, -1):
        a[i] = a[i-1]
    a[0] = last


rotateArray(a)
print(a)


# ------------------------- Rearrange Array -------------------------

# sort array and add -1 where missing number
c = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

init = 0

for i in range(0, len(c)):
    for j in c:
        if j == init:
            index = c.index(j)
            c[init], c[index] = c[index], c[init]
    init += 1

print(c)


# ------------------------- Array | Range Query -------------------------

d = [1, 2, 3, 4, 5]

r1 = [1, 3]
r2 = [2, 4]

sum = 0
for i in range(r2[0], r2[1]+1):
    sum += d[i]
print(sum)


# ------------------------- Kadane’s Algorithm -------------------------

def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0

    print(f'--- {max_so_far} - {max_ending_here}')
    for i in range(0, size):

        max_ending_here = max_ending_here + a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(a, len(a)))

# ------------------------- Dutch National Flag -------------------------

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
