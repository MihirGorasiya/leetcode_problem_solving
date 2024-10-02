a = "11"
b = "1"

a = "1010"
b = "1011"

i = len(a) - 1
j = len(b) - 1
carry = 0
ans = ""
while i >= 0 or j >= 0:
    m = a[i] if i >= 0 else "0"
    n = b[j] if j >= 0 else "0"
    print(f'{m} + {n} + {carry}')
    if m == "1" and n == "1" and carry == 0:
        ans = "0" + ans
        carry = 1
    elif m == "1" and n == "1" and carry == 1:
        ans = "1" + ans
        carry = 1
    elif m == "0" and n == "0" and carry == 1:
        carry = 0
        ans = "1" + ans
        
    elif m == "0" and n == "0" and carry == 0:
        ans = "0" + ans
        
    elif ((m == "1" and n == "0") or (m == "0" and n == "1")) and carry == 0:
        ans = "1" + ans
        
    elif ((m == "1" and n == "0") or (m == "0" and n == "1")) and carry == 1:
        ans = "0" + ans
        carry = 1
    print(f'{ans} _ {carry}')
    i -= 1
    j -= 1
if carry == 1:
    ans = "1" + ans

print(ans)
