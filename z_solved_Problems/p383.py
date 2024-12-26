from collections import Counter

ransomNote = "a"
magazine = "b"

# ransomNote = "aa"
# magazine = "aab"
ransomNote = "aa"
magazine = "ab"

charsInRansomNote = dict(Counter(ransomNote))
charsInMagazine = dict(Counter(magazine))

ans = True
for i in charsInRansomNote:
    
    if i not in charsInMagazine or charsInRansomNote[i] > charsInMagazine[i]:
        ans = False

print(ans)
