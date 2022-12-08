function print(object) {
    console.log(object);
}

var maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
var entrance = [1, 2]

var exits = []

var m = maze.length;
var n = maze[0].length;

for (let i = 0; i < m; i++) {
    if (maze[i][0] == '.' && !isEntrance(i, 0))
        exits.push([i, 0]);
    if (maze[0][i] == '.' && !isEntrance(0, i))
        exits.push([0, i]);
}
if (maze[m - 1][n - 1] == '.' && !isEntrance(m - 1, n - 1))
    exits.push([m - 1, n - 1]);

function isEntrance(a, b) {
    if (a == entrance[0] && b == entrance[1])
        return true
    else
        false
}

for (let i = 0; i < exits.length; i++) {
    
}

print(exits);