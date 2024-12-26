n = 2
# 1 1 2 3 5 8 13 
fib = [1] * (n + 1)


def fibonacci(n, fib):
    if n == 1:
        return 1
    elif n ==0:
        return 0
    else:
        if fib[n] != 1:
            return fib[n]
        else:
            fib[n - 1] = fibonacci(n - 1, fib)
            fib[n - 2] = fibonacci(n - 2, fib)
            return fib[n - 1] + fib[n - 2]


print(fib)
print(fibonacci(n, fib))
