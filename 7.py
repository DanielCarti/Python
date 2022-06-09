def main(x):
    A = x & 0b1111111111
    B = (x >> 10) & 0b1111111
    C = (x >> 17) & 0b111111111111
    D = (x >> 29) & 0b11
    E = (x >> 31) & 0b1

    result = 0
    result |= C
    result |= A << 12
    result |= E << 22
    result |= B << 23
    result |= D << 30
    return result

print(hex(main(0x55aaccea)))