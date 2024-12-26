s = 'babad'

length = len(s)+1
answer = ''
start = 0


def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


for i in range(0, length):
    tmp = helper(s, i, i)
    if len(tmp) > len(answer):
        answer = tmp

    tmp = helper(s, i, i+1)
    if len(tmp) > len(answer):
        answer = tmp


print(answer)
