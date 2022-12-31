function print(object) {
    console.log(object);
}

// var s = 'PAYPALISHIRING'
var s = 'A'
var numRows = 1;
if (numRows == 1)
    return s
var divideNum = (numRows + (numRows - 2))

var ans = ''

for (let i = 0; i < numRows; i++) {
    for (let j = 0; j < s.length; j++) {
        if ((j % divideNum) == divideNum - i || (j % divideNum) == i) {
            ans += s[j]
        }
    }
}
print(`${ans}`)