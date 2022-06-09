import math as m


def main(x, z, y):
    return m.sqrt(((5 * x ** 2 + 29 * x ** 3 +
                    54) ** 3 + 85 * (39 * y ** 2 - z ** 3 - 1) ** 5) /
                  (((m.log(z**3 + y**2 + 0.02)**6) / 51) +
                   x**4)) - m.sqrt(y**3 - (z+x**3)**4)


print('%.2e' % main(-0.72, 0.81, 0.35))
