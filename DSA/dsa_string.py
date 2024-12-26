# ------------------------- Substring -------------------------

# Number of substrings of one string present in other
'''
s1 = 'abcd'
s2 = 'swalencud'

ans = 0

for i in range(len(s1)):
    for j in range(i, len(s1)):
        if s2.find(s1[i:j+1]) != -1:
            ans += 1

print(ans)
'''

# Print all substring of a number without any conversion
'''
# n = '123'

# for i in range(len(n)):
#     for j in range(i, len(n)):
#         print(n[i:j+1])
'''


# Substring Reverse Pattern
# Input: str = “first”
# Output:
# first
# *sri*
# **r**
'''
str = 'geeks'
reversedStr = ''
ans = [str]

def reverseStr(s):
    global ans
    f = 0
    l = len(s)-1
    while (f < l):
        s[f], s[l] = s[l], s[f]
        f += 1
        l -= 1
    return ''.join(s)

def replaceChar(s, char):
    f = 0
    l = len(s)-1
    
    while f < l:
        s[f] = char
        s[l] = char
        f+=1
        l-=1
        ans.append(''.join(s))

reversedStr = reverseStr(list(str))

replaceChar(list(reversedStr), '*')

for i in ans:
    print(i)
'''
