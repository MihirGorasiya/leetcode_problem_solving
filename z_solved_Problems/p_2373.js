function print(obj) {
    console.log(obj);
}

function max(a, b, c) {
    if (a > b) {
        if (a > c)
            return a;
        else
            return c;
    }
    else {
        if (b > c)
            return b;
        else
            return c;
    }
}

grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
// grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
len = grid.length
ans = []
for (let i = 1; i < len - 1; i++) {
    x = []
    for (let j = 1; j < len - 1; j++) {
        x.push(max(
            max(grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1]),
            max(grid[i][j - 1], grid[i][j], grid[i][j + 1]),
            max(grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]),
        ))
    }
    ans.push(x)
}
