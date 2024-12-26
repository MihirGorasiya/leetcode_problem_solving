s = "IceCreAm"

s = "leetcode"

asciis = {65, 69, 73, 79, 85, 97, 101, 105, 111, 117}
vowels = []
res = ""
tempRes = ""
for char in s:
    if ord(char) in asciis:
        vowels.append(char)

i = len(vowels) - 1
for char in s:
    if ord(char) in asciis:
        res += vowels[i]
        i -= 1
    else:
        res += char

print(res + tempRes)
