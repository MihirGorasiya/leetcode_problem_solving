function print(object) {
    console.log(object);
}
var digits = [6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]
var s = ''
var ans = []
s = digits.join('')
print(s)
var t = BigInt(s)
print(t)
t = t+BigInt(1)
print(t)
s = t.toString()

var ansString = []
for (let i = 0; i < s.length; i++) {
    ansString.push(parseInt(s[i]))
}
print(ansString)