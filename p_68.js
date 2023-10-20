function print(object) {
    console.log(object);
}

var words = ["This", "is", "an", "example", "of", "text", "justification."];
// var words = ["What", "must", "be", "acknowledgment", "shall", "be"];
var maxWidth = 16


function spacess(length) {
    var ret = '';
    for (let i = 0; i < length + 1; i++) {
        ret += ' ';
    }
    // print(`'${ret}'`)
    return ret;
}

var lines = ['']
var lineIndex = 0
for (let o = 0; o < words.length; o++) {
    if (lines[lineIndex].length + words[o].length < maxWidth - 1) {
        if (lines[lineIndex].length == 0)
            lines[lineIndex] += (words[o])
        else
            lines[lineIndex] += (' ' + words[o])
    }
    else {
        lines.push(words[o])
        lineIndex++
    }

}

for (let i = 0; i < lines.length; i++) {
    var rSpaces = maxWidth - lines[i].length

    if (i < lines.length - 1) {
        if (lines[i].includes(' ')) {
            if (rSpaces % 2 == 0) {
                var spl = lines[i].split(' ');
                lines[i] = lines[i].replaceAll(' ', spacess(rSpaces / (spl.length - 1)));
            }
            else {
                print(8 % 3)
            }
        }
        else
            lines[i] = lines[i] + spacess(rSpaces - 1);
    }
    else {
        //for last line
        lines[lines.length - 1] = lines[lines.length - 1] + spacess(rSpaces - 1)
    }
}
print(lines[1].length)
print(lines)
