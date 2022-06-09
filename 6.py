s = {
    'SQLPL': {
        'MINID': {
            'X10': 0,
            'YANG': {
                'PHP': 1,
                'LESS': 2,
                'FORTH': 3
            }
        },
        'ASN.1': 10
    },
    'ADA': {
        'MINID': {
            'GLYPH': 5,
            'EJS': 6,
            'NINJA': 7
        },
        'ASN.1': {
            'GLYPH': 8,
            'EJS': {
                'PHP': 9,
                'LESS': 10,
                'FORTH': 11
            },
            'NINJA': 12
        }
    }
}


def main(path):
    s1 = s[path[2]]
    if path[2] == 'SQLPL':
        s2 = s1[path[3]]
        if path[3] == 'MINID':
            s3 = s2[path[0]]
            if isinstance(s3, int):
                return s3
            return s3[path[1]]
        return 4
    else:
        s2 = s1[path[3]]
        if path[3] == 'ASN.1':
            s3 = s2[path[4]]
            if path[4] == 'GLYPH':
                return 8
            elif path[4] == 'NINJA':
                return 12
            else:
                return s3[path[1]]
        else:
            return s2[path[4]]


print(main(['YANG', 'PHP', 'SQLPL', 'ASN.1', 'GLYPH']))
