numerator = 1
denominator = 2


def fractionToDecimal(numerator, denominator):
    if numerator == 0:
        return "0"

    result = []
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")

    num = abs(numerator)
    denom = abs(denominator)
    remainder = num % denom
    result.append(str(num // denom))

    if remainder == 0:
        return "".join(result)

    result.append(".")
    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            result.insert(remainder_map[remainder], "(")
            result.append(")")
            break

        remainder_map[remainder] = len(result)

        remainder *= 10
        result.append(str(remainder // denom))
        remainder %= denom
    return "".join(result)


if __name__ == "__main__":
    cases = [[1, 2], [2, 1], [4, 333]]
    answers = []
    for i in range(len(cases)):
        print(fractionToDecimal(cases[i][0], cases[i][1]))
