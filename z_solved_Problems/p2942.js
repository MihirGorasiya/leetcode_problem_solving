function print(obj) {
    console.log(obj);
}


words = ["abc", "bcd", "aaaa", "cbc"]
x = "a"
ans = []
for (let i = 0; i < words.length; i++) {
    print(i)
    if (words[i].includes(x))
        ans.push(i)
}

print(ans)