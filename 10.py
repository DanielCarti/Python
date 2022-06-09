row_1 = ['None', 'Олег Л. Сиголян', 'sigolan[at]yahoo.com',
         'None', 'Да', '0.2', ]
row_2 = ['None', 'Всеволод Б. Шадяк', 'vsevolod3[at]yahoo.com',
         'None', 'Да', '0.5', ]
row_3 = []
row_4 = []
row_5 = ['None', 'Елисей С. Шаляк', 'elisej84[at]mail.ru',
         'None', 'Нет', '1.0', ]


table = [row_1, row_2, row_3, row_4, row_5, ]
not_empty = [i for i in table if len(i) != 0]
for r in not_empty:
    if len(r) == 0:
        del r
for r in not_empty:
    while "None" in r:
        r.remove("None")

for r in not_empty:
    for i in range(len(r)):
        if r[i].count(' ',) > 1:
            r[i] = var = r[i][r[i].find('. ') + 2:] + ' ' + r[i][0] + \
                         '.' + r[i][r[i].find('. ') - 1] + '.'
        elif '[at]' in r[i]:
            r[i] = r[i].replace('[at]', '@')
            continue
        elif r[i] == 'Да' or r[i] == 'Нет':
            if r[i] == 'Да':
                r[i] = 'Выполнено'
                continue
            elif r[i] == 'Нет':
                r[i] = 'Не выполнено'
                continue
        elif '.' in r[i]:
            r[i] = str(int(round(float(r[i]), 1)*100))+'%'
            continue

for r in not_empty:
    print(r)
