import math as m


def main(a, n, x):
    result = 0
    for k in range(1, a+1):
        s += (4 * k ** 2 - k - (28 + 13 * k ** 3) ** 6)
        for c in range(1, n+1):
            s1 += (m.fabs(72 * c ** 2 - 27 * x ** 3 - (x/40))) ** 3/99
        s += s1
        result += s
    return result

