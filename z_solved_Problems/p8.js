function print(object) {
    console.log(object);
}

var s = '+-42'
var ans = 0

if (Number.isNaN(parseInt(s)))
    ans = 0
else
    ans = parseInt(s)


if (ans < -2147483648)
    return -2147483648;
else if (ans > 2147483647)
    return 2147483647;


print(ans)