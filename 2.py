import math as m


def main(z):
    if z < 181:
        return z**5 - z
    if 181 <= z < 217:
        return z**4 / 9
    if 217 <= z < 310:
        return 44*z
    else:
        return (abs(z**3 + 42*z**2))**3 - 40 - z**6


print('%.2e' % main(340))
