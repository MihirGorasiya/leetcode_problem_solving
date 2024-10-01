s = "baa"
p = "b*"
s = "cb"
p = "?a"
s = "adceb"
p = "*a*b"
s = "a"
p = "aa"
s = ""
p = "******"
chars = [*s[::-1]]

for i in range(len(p)):
    if len(chars)==0:
        break
        
    if p[i] == '*':
        if i == len(p)-1:
            chars = []
        else:
            while len(chars)>0 and chars[-1] != p[i+1]:
                chars.pop()
        continue
    elif p[i] == '?':
        chars.pop()
    else:
        if chars[-1] == p[i]:
            chars.pop()
        else: 
            break
           

if len(chars)==0:
    print('True')
else:
    print('False')
    