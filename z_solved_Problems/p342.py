n = 5


def power_of_four(n):
    if n == 1:
        return True
    elif n < 0:
        return False
    elif n % 4 == 0:
        return power_of_four(n // 4)
    else:
        return False


print(power_of_four(n))
