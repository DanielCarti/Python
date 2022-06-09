def main(a, n, b):
    result = 0
    for i in range(1, b+1):
        s = 0
        for c in range(1, n+1):
            s1 = 0
            for k in range(1, a+1):
                s1 += (24*c + (k**3/24))**2 - (1 - 40*k - 66*i**3)**6
            s += s1
        result += s
    return result

print('%.2e' % main(8, 7, 8))