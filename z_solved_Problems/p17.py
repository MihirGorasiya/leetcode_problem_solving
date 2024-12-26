digits = "234"
# digits = "5"

digitToChar = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "": "",
}
res = []
if len(digits) <= 1:
    print(list(digitToChar[digits]))
else:
    for i in digits:
        if len(res) == 0:
            res.extend(list(digitToChar[i]))
        else:
            temp = []
            for j in digitToChar[i]:
                for k in res:
                    temp.append(f"{k}{j}")

            res = temp
print(res)
