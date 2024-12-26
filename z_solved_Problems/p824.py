sentence = "I speak Goat Latin"
vowel = {
    "a",
    "e",
    "i",
    "o",
    "u",
    "A",
    "E",
    "I",
    "O",
    "U",
}
currentWordIndex = 1
firstChar = sentence[0]
currentWord = ""
res = ""
for i in range(len(sentence)):
    print(sentence[i])
    if sentence[i] == " ":
        if firstChar in vowel:
            currentWord += "ma" + "a" * currentWordIndex + " "
        else:
            currentWord += firstChar + "ma" + "a" * currentWordIndex + " "
        res += currentWord
        currentWord = ""
        currentWordIndex += 1
        firstChar = ""
    elif firstChar == "":
        firstChar = sentence[i]
    else:
        currentWord += sentence[i]


if firstChar in vowel:
    currentWord += "ma" + "a" * currentWordIndex + " "
else:
    currentWord += firstChar + "ma" + "a" * currentWordIndex + " "
print(res + currentWord)
# if sentence[i] in vowel:
