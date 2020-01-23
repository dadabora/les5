import json
try:
    f_r = open(r"zad7.txt", 'w')
    f_r.write("Фирма-А ООО 10000 5000 \n"
              "Фирма-Б ОАО 143223 143224 \n"
              "Фирма-В ООО 102020 70043")
    f_r.close()
except IndentationError:
    print('')

firm_list = []
pr = 0
f_r = open(r"zad7.txt", 'r')
a = 0
b = 0
dict_1 = {}

for line in f_r:


    o = list(line.split(' '))

    z = int(o[2]) - int(o[3])
    firm_list.append(line.rstrip())
    dict_1[o[0]] = z
    if z < 0:
        z ="Нет прибыли"
        b += 1
    else:
        pr = pr + z
    print(firm_list[a],' - ', z)
    a += 1
b = len(firm_list) - b
dict_2 = {"Средняя прибыль": pr/b}
print('Средняя прибыль равна = ', pr/b)
f_r.close()
json_list = [dict_1, dict_2]
print(json_list)
with open("my_file.json", "w") as write_f:
    json.dump(json_list, write_f)