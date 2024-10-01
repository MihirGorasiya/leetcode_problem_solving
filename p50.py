x = 2.00000
n = 10
# x = 2.10000
# n = 3
x = 0.00001
n = 2147483647
x = 2.00000
n = -2

def power(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1

    ans = power(x, n // 2)
    ans = ans * ans

    if not n % 2:
        ans = ans * x


ans = pow(x, n)
print(ans)
print(1/ans)
if n >= 0:
    print(ans)
else:
    print(n)
    print(1 / ans)
