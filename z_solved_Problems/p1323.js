var num = 6699
var numString = num.toString()
var maxNum = num

for (let i = 0; i < numString.length; i++) {
    if (numString[i] == '9') {
        continue
    }
    else {
        var tempString = numString.replace("6", "9")
        var tempMax = parseInt(tempString)
        if (tempMax > maxNum)
            maxNum = tempMax
    }
}

return maxNum