words = ["USA", "FlaG", "leetcode", "letCode", "Google", "G", "g", "mL"]


def detectCap(word):
    l = len(word)
    if(l==1):
        return True
    i = 2
    firstCap = ord(word[0]) > 64 and ord(word[0]) < 91
    secondCap = ord(word[1]) > 64 and ord(word[1]) < 91
    
    if (not firstCap and secondCap):
        return False

    while i < l:
        if (firstCap and secondCap) and (ord(word[i]) > 96 and ord(word[i]) < 123):
            return False
        if (firstCap and not secondCap) and (ord(word[i]) > 64 and ord(word[i]) < 91):
            print(f"{word} {word[i]} {i}")
            return False
        if (not firstCap and not secondCap) and (
            ord(word[i]) > 64 and ord(word[i]) < 91
        ):
            return False

        i = i + 1

    return True


for i in words:
    print(f"{i} - {detectCap(i)}")
