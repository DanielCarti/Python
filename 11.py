import struct as st


def main(x):
    return a(x, 4)


def a(x, start):
    return {
        'A1': [b(x, address_b(x, start)),
               b(x, address_b(x, start + 4)),
               b(x, address_b(x, start + 8)),
               b(x, address_b(x, start + 12)),
               b(x, address_b(x, start + 16))],
        'A2': c(x, address_c(x, start + 20)),
        'A3': st.unpack('< f', x[start + 24:start + 28])[0],
        'A4': d(x, address_d(x, start + 28)),
        'A5': st.unpack('< q', x[start + 30:start + 38])[0]
    }


def address_d(x, start):
    return st.unpack('< H', x[start:start + 2])[0]


def address_c(x, start):
    return st.unpack('< I', x[start:start + 4])[0]


def address_b(x, start):
    return st.unpack('< I', x[start:start + 4])[0]


def b(x, start):
    return {
        'B1': st.unpack('< I', x[start:start + 4])[0],
        'B2': str(st.unpack('< c', x[start + 4:start + 5])[0])[
                  2] + str(st.unpack('< c', x[start + 5:start + 6])[0])[
            2] + str(st.unpack('< c', x[start + 6:start + 7])[0])[
                  2] + str(st.unpack('< c', x[start + 7:start + 8])[0])[
            2] + str(st.unpack('< c', x[start + 8:start + 9])[0])[
            2] + str(st.unpack('< c', x[start + 9:start + 10])[0])[
                  2] + str(st.unpack('< c', x[start + 10:start + 11])[0])[
            2] + str(st.unpack('< c', x[start + 11:start + 12])[0])[2],
    }


def c(x, start):
    return {
        'C1': uint16_uint32_double(x, start),
        'C2': st.unpack('< h', x[start + 6:start + 8])[0],
        'C3': st.unpack('< i', x[start + 8:start + 12])[0],
        'C4': st.unpack('< Q', x[start + 12:start + 20])[0],
        'C5': st.unpack('< Q', x[start + 20:start + 28])[0],
        'C6': st.unpack('< i', x[start + 28:start + 32])[0],
    }


def uint16_uint32_double(x, start):
    size = st.unpack('< H', x[start:start + 2])[0]
    address = st.unpack('< I', x[start + 2:start + 6])[0]
    arr = st.unpack('< ' + 'd' * size, x[address:address + 8 * size])
    return list(arr)


def d(x, start):
    return {
        'D1': [
            st.unpack('< d', x[start:start + 8])[0],
            st.unpack('< d', x[start + 8:start + 16])[0],
        ],
        'D2': st.unpack('< h', x[start + 16:start + 18])[0],
        'D3': st.unpack('< f', x[start + 18:start + 22])[0]
    }


def main(x):
    return a(x, 4)


print(main(b'LUY\x80*\x00\x00\x006\x00\x00\x00B\x00\x00\x00N\x00\x00\x00Z\x00\x00\x00'
           b'v\x00\x00\x005\x087?\x96\x00$n\xe9\x01y\xd5\xc85\xa4;\xcc\xf7elhqwmsk>\xb6'
           b'\xdfCnkfzydue\xa3\rH\x9bgebzazbc\xb3g\xf1tyjnvwyhp\x1bW\xbb\xd8ezorjvkq\xa6}'
           b',l\x05n\xe6\xbfp5\xc0+\x15\xb2\xc9\xbf\x02\x00f\x00\x00\x00\xfb\r\x99\xdd'
           b'\xfcP\xcct\xf9\x99\x16<d\xe5\x1c\xb8H\xdaR\xf4`<(\x96\xe8\xb4<\xee\xe9R7\xbe'
           b'\xd1\xbf\x00\x01\x8d\xb7\xedj\x9e\xbfq\x92\x97\xb3\xa0\xbe'))
