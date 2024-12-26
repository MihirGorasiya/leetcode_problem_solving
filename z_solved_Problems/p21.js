var list1 = [1, 2, 4]
var list2 = [1, 3, 4]

var temp = []
for (let i = 0; i < list1.length; i++) {
    temp.push(list1[i])
}
for (let i = 0; i < list2.length; i++) {
    temp.push(list2[i])
}

console.log(temp);
temp.sort()
console.log(temp);
console.log(temp.length);
// var dvsj = temp.length
// console.log(dvsj);