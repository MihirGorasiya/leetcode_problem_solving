var s = 'foo'
var t = 'bar'

var s_chars = []
var t_chars = []

var answer = ''

for (let i = 0; i < s.length; i++) {
    if (!s_chars.includes(s[i]))
        s_chars.push(s[i])

    if (!t_chars.includes(t[i]))
        t_chars.push(t[i])
}

for (let i = 0; i < s.length; i++) {

    if (t_chars[s_chars.indexOf(s[i])] != t[i]) {
        answer = 'false'
    }

}
if (answer == '')
    answer = 'true'
console.log(answer)