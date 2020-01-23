#Задание номер один
print("Это задание первое, вам надо ввести несколько строк состоящих из"
      " нескольких слов, для того чтобы выполнилось задание номер 2")
while True:
    my_f = open("text.txt", "a")
    new_ctr = input('Новая строка - ')
    if new_ctr == '':
        my_f.close()
        break


    my_f.write(new_ctr+'\n')

#Задание номер два
my_f = open("text.txt", "r")
a = 0
word = 0
for line in my_f:
    a += 1
    o = len(list(line.split(' ')))
    word = word + o
    print(a,'строка', o,"слов --", line)

print(a, 'строк в файле и', word, 'слов' )
my_f.close()