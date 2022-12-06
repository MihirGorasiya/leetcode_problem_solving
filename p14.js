function print(object) {
    console.log(object);
}
// var strs = ["flower", "flower", "flower", "flower"]
var strs = ['ab', 'a']
if (strs[0] == "")
    return ""
if (strs.length == 1)
    return strs[0]

var prifix = '';
prifix = strs[0].substring(0, 1);
var isSamePrifix = true;
var j = 1;
var i = 0;
while (isSamePrifix) {
    while (i < strs.length) {
        if (!strs[i].startsWith(prifix)) {
            prifix = strs[0].substring(0, j - 1);
            isSamePrifix = false;
            break;
        }
        i++
    }
    i = 0;
    if (prifix == strs[0])
        return strs[0]
    if (!isSamePrifix)
        break


    j++;
    prifix = strs[0].substring(0, j);
}

print('answer:' + prifix);