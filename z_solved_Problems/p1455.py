sentence = "i love eating burger"
searchWord = "burg"

sentence = "this preblem is an easy problem"
searchWord = "problem"
sentence = "hellohello hellohellohello"
searchWord = "ell"

m = 0
n = len(searchWord) - 1
wordCount = 1
checkWord = True

i = 0
while i < len(sentence):
    if checkWord and sentence[i] != searchWord[m]:
        print(f"! {sentence[i]} - {searchWord[m]} | {checkWord}")
        m = 0
        checkWord = False
    elif checkWord and sentence[i] == searchWord[m] and m < n:
        print(f"{sentence[i]} - {searchWord[m]} | {checkWord}")
        m += 1

    if m == n:
        print(f"word match at {wordCount}")
    if sentence[i] == " ":
        wordCount += 1
        checkWord = True
    i += 1

print(wordCount)
