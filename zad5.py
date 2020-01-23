
try:
    f_r = open(r"zad5.txt", 'w')
    f_r.write("324 44 32 2234 4324 4234 4234 4234")
    f_r.close()
except IndentationError:
    print('')
a = 0
o = []
f_r = open(r"zad5.txt", 'r')
for line in f_r:
    a += 1


    o = list(line.split(' '))

o = [int(el) for el in o]
print(sum(o))
f_r.close()
