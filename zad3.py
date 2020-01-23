

a = 0
work = 0
min_20 = []
my_fa = open("oklad.txt", "r")
for line in my_fa:
    a += 1

    line_min = line[:-1]
    o = list(line_min.split(' '))
    print(o[0], o[1])
    work = work + int(o[1])
    min_20.append(o[0])

    if int(o[1]) <= 20000:
        print('\t','меньше 20000-',o[0],o[1])
print(int(work/a), '- средняя зарплата всех сотрудников')
print(min_20 , "меньше 20000" )
my_fa.close()