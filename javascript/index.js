function print(object) {
    console.log(object);
}

var s = 'aa';
var p = 'a*';
var tempStrings = [];

if (p.includes('*') || p.includes('.')) {
    if (p.includes('*')) {
        var position = p.indexOf('*');
        print(position);
        if (p.length==2) {
            for (let i = 0; i < 20; i++) {
                tempStrings.push(`${p[0]}`)

            }
        }
    }
}
else {
    if (s == p)
        print(true);
    else
        print(false);
}