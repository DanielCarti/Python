import math as m


def main(y, x, z):
    n = len(y)
    result = 0
    for i in range(1, n+1):
        result += 47 * m.sin(y[n-m.ceil(i/2)] - z[i-1]**3 - x[n-i]**2) ** 5
    return result


print('%.2e' % main([-0.26, -0.78, 0.22, 0.41, -0.15], [0.37, 0.81, 0.62, -0.31, 0.81], [-0.09, -0.06, -0.48, 0.04, 0.07]))
