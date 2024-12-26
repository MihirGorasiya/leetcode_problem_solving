s = "A man, a plan, a canal: Panama"

# 48 - 57 | 97 - 122

def checkPel(s):
    newS = s.lower()

    i = 0
    j = len(s) - 1
    while i < j:
        if (ord(newS[i]) < 48 or ord(newS[i]) > 57) and (ord(newS[i]) < 97 or ord(newS[i]) > 122):
            print(newS[i])
            i = i + 1
            continue
        if (ord(newS[j]) < 48 or ord(newS[j]) > 57) and (ord(newS[j]) < 97 or ord(newS[j]) > 122):
            print(ord(newS[j]))
            j = j - 1
            continue
        print(f"{i}  {newS[i]}  {j} {newS[j]}")
        if newS[i] != newS[j]:
            return False

        i = i + 1
        j = j - 1

    return True


print(checkPel(s))