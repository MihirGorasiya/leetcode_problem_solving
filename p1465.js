function print(object) {
    console.log(object);
}

var h = 1000000000
var w = 1000000000
// var horizontalCuts = [3]
// var verticalCuts = [3]
var horizontalCuts = [2]
var verticalCuts = [2]
var maxHeight = 0
var maxWidth = 0
horizontalCuts.sort()
verticalCuts.sort()

maxHeight = Math.max(horizontalCuts[0], h - horizontalCuts[horizontalCuts.length - 1])
for (let i = 1; i < horizontalCuts.length; i++) {
    maxHeight = Math.max(maxHeight, horizontalCuts[i] - horizontalCuts[i - 1])
}

maxWidth = Math.max(verticalCuts[0], w - verticalCuts[verticalCuts.length - 1])

for (let i = 1; i < verticalCuts.length; i++) {
    maxWidth = Math.max(maxWidth, verticalCuts[i] - verticalCuts[i - 1])
}

print(BigInt(maxHeight) * BigInt(maxWidth) % 1000000007n)