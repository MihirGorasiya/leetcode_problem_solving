s = "ADOBECODEBANC"
t = "ABC"

seen = {"BANC"}


def checkSubString():
    return any(t in s for s in seen)


print(checkSubString())
