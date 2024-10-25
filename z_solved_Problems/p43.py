num1 = "2"
num2 = "3"

num1 = "123"
num2 = "456"
num1 = "9"
num2 = "9999"

strToInt = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}
n1 = 0
n2 = 0

length = len(num1) - 1
for i in range(len(num1)):
    n1 += 10 ** (length - i) * strToInt[num1[i]]
    
length = len(num2) - 1
for i in range(len(num2)):
    n2 += 10 ** (length - i) * strToInt[num2[i]]

print(n1)
print(n2)
print(n1 * n2)
