function print(obj) {
    console.log(obj);
}


items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"


rules = { "type": 0, "color": 1, "name": 2 }
ans = []
for (i = 0; i < items.length; i++) {
    if (items[i][rules[ruleKey]] == ruleValue) {
        ans.push(items[i])
    }
}
print(ans.length)