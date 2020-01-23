def int_sort(z):
    o = list(z)
    v = '0'
# фильтр  отличных от цифр знаков
    for a in o:

        if a.isdigit() == False:
            continue
        v = v + a


    v = int(v)
    return v
# Ввожу потому что не получилось разобраться с encoding при вводе в txt в коде абракадабра
try:
    f_r = open(r"zad6.txt", 'w')
    f_r.write("Информатика: 200(л) 50(пр) 20(лаб) \n"
              "Физика: 30(л) — 10(лаб) \n"
              "Физкультура: — 30(пр) — ")
    f_r.close()
except IndentationError:
    print('')
yr_dict = {}
f_r = open(r"zad6.txt", 'r')
for line in f_r:
    print(line)
    #разбиение строк на списки и отправка каждого значения на фильтр символов
    o = list(line.split(' '))
    z = int_sort(o[1]) + int_sort(o[2]) + int_sort(o[3])
    yr_di = {o[0]:z}
    yr_dict.update(yr_di)

print(yr_dict)
f_r.close()