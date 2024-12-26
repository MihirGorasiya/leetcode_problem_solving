s = "abcd"
t = "abcde"

chars = {}

for char in t:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1

for char in s:
    if chars[char] > 1:
        chars[char] -= 1
    elif char in chars:
        chars.pop(char)
    else:
        break
print(chars)
print(list(chars.keys())[0])
