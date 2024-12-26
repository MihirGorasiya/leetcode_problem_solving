words = ["pay", "attention", "practice", "attend"]
pref = "at"

count = 0
prefLen = len(pref)
for word in words:
    if word[0:prefLen] == pref:
        count += 1

print(count)
