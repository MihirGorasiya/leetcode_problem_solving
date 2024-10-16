s = "()[]{}"
# s = "(]"
# s = "([])"
# s = "()"
s = "([)]"

bracketChecker = []
j = -1
for i in range(len(s)):
    if ord(s[i]) == 40 or  ord(s[i]) == 91 or  ord(s[i]) == 123:
        bracketChecker.append(s[i])
        j+=1
        continue
    if j==-1 and (ord(s[i]) == 41 or ord(s[i]) == 93 or ord(s[i]) == 125):
        print('False')
    if ord(s[i]) == 41 and ord(bracketChecker[j]) == 40:
        bracketChecker.pop()
        j-=1
    elif ord(s[i]) == 93 and ord(bracketChecker[j]) == 91:
        bracketChecker.pop()
        j-=1
    elif ord(s[i]) == 125 and ord(bracketChecker[j]) == 123:
        bracketChecker.pop()
        j-=1
    else:
        print('False')
print(len(bracketChecker)==0)
