var operations = ["--X", "X++", "X++"];
var X = 0;

for (let i = 0; i < operations.length; i++) {
    X = performOperation(X, operations[i]);
}
return X


function performOperation(X, operation) {
    switch (operation) {
        case '++X':
            X = X + 1;
            break;
        case 'X++':
            X = X + 1;
            break;
        case '--X':
            X = X - 1;
            break;
        case 'X--':
            X = X - 1;
            break;

        default:
            break;
    }

    return X;
}