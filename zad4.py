a = 0
ru_list = ['один', 'два', 'три', 'четыре']
with open("zad4.txt") as f_en:
    for line in f_en:
        o = list(line.split(' '))
        print(ru_list[a], o[1], o[2] , file = open("zad4ru.txt", "a"))
        a +=1

f_ru = open("zad4ru.txt", 'r')
content = f_ru.read()
print(content)
f_ru.close()