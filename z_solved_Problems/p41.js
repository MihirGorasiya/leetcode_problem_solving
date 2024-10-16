function print(obj) {
    console.log(obj);
}
var nums = [1, 0]

nums.sort((a, b) => a - b)
var min = 1

for (let i = 0; i < nums.length; i++) {
    if (min === nums[i]) {
        min++
    }
}

print(min)
