n = 17


def power(n):
    if n == 1:
        return True
    elif n < 0:
        return False
    if n % 2 == 0:
        return power(n // 2)
    else:
        return False

print(power(n))