words = ["Hello", "Alaska", "Dad", "Peace"]

row1 = set("qwertyuiop")
row2 = set("asdfghjkl")
row3 = set("zxcvbnm")

res = []

for word in words:
    lower_word = word.lower()
    if lower_word[0] in row1:
        keyboardRow = row1
    elif lower_word[0] in row2:
        keyboardRow = row2
    else:
        keyboardRow = row3

    for char in lower_word:
        if char not in keyboardRow:
            break
    else:
        res.append(word)

print(res)
