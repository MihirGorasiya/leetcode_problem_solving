pattern = "abba"
# pattern = "aaaa"
s = "dog cat cat dog"
# s = "dog cat cat fish"

words = s.split(" ")
if len(pattern) != len(words):
    print(False)

seen = {}
length = len(words)
i = 0

while i < length:
    if pattern[i] in seen and seen[pattern[i]] != words[i]:
        print(False)
    else:
        for key in seen:
            if (words[i] == seen[key] and key != pattern[i]) or (
                pattern[i] == key and words[i] != seen[key]
            ):
                print(False)

        seen[pattern[i]] = words[i]
    i += 1
print(True)
