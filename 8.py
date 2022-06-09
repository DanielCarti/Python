def main(s: str):
    res = {}
    s = s.replace('|', '')
    s = s.replace('data', '')
    s = s.replace('q(', '')
    s = s.replace(')', '')
    s = s.replace('{', '')
    s = s.replace('};', '')
    s = s.replace(' ', '')
    s = s.replace(':=', ';')
    s = s.replace('\n', '')
    counter = 0
    for el in s.split(';'):
        if counter == 2:
            res[key] = value
            counter = 0
        if ',' in el:
            value = list(map(int, el.split(",")))
            counter += 1
        else:
            key = el
            counter += 1
    return res


print(main('| data q(ceisbi_941) := { -2309, -4323,-1242};|;| data q(orxe):= {4594 , 262 }; |;'))
