s = '{({[{]})}'

pair = {')': '(', '}': '{', ']': '['}
opening = ['(', '{', '[']
closing = [')', '}', ']']

output = []

def contains(array, ch):
    for i in array:
        if ch == i:
            return True
    return False

for i in s:
    if contains(opening, i):
        output.append(i)
    else:
        if output[-1] == pair[i]:
            output.pop()

if len(output) == 0:
    print('balanced')
else:
    print('Not balanced')
