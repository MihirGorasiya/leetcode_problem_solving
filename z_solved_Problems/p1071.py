str1 = "ABCABC"
str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"

# str1 = "ABCDEF"
# str2 = "ABC"

# str1 = "LEET"
# str2 = "CODE"

if str1[0] != str2[0]:
    print("")

if len(str1) > len(str2):
    maxString = str1
    minString = str2
else:
    maxString = str2
    minString = str1

max_length = len(maxString)
min_length = len(minString)

i = 0
j = 1
while i < min_length:
    if minString[i] == minString[0] and minString[0:j] == minString[i : i + j]:
        i += j - 1
    else:
        j += 1

    if str1[i] != str2[i]:
        print("not same")
    i += 1

print(str1[0:j])
i = 0
while i < max_length:
    if maxString[0:j] != maxString[i : i + j]:
        print(f"{maxString[0:j]} != {maxString[i : i + j]}")
        print("not same22")
    i += j 


