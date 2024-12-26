n = 30
k = 434991989
# n = 4
# k = 6


def kthGrammar(n, k):
    if n == 1:
        print(f"{n} _ {k}")
        return 0

    mid = 2 ** (n - 1) // 2

    if k <= mid:
        return kthGrammar(n - 1, k)
    else:
        return 1 - kthGrammar(n - 1, k - mid)


print(n, k)
