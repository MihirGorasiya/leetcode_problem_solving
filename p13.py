s = "MCMXCIV"
s = "IV"
s = "IX"
# s = "LVIII"
# s = "MCMXCIV"
# s = "XXI"
# s = "C"
# s = "XL"
# s = "DCCC"
# s = "MMXX"


romanNumber = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
ans = 0
i = 0
while i < len(s):
    if i + 1 < len(s):
        if (
            (s[i] == "I" and s[i + 1] == "V")
            or (s[i] == "I" and s[i + 1] == "X")
            or (s[i] == "C" and s[i + 1] == "D")
            or (s[i] == "C" and s[i + 1] == "M")
            or (s[i] == "X" and s[i + 1] == "L")
            or (s[i] == "X" and s[i + 1] == "C")
        ):
            
            ans += romanNumber[s[i + 1]] - romanNumber[s[i]]
            i += 2
            continue
    ans += romanNumber[s[i]]
    i += 1
print(ans)
