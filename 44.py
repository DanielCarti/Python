import math as m


def main(n):
    if n == 0:
        return -0.01
    if n >= 1:
        return m.sin(13 * main(n-1) ** 3 - 32 - main(n-1)) ** 2


print('%.2e' % main(8))
