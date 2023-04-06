import random
letters = 'qwertyuioplkjhgfdsazxcvbnm'

lista = []
for i in letters:
    lista.append(i)

random.shuffle(lista)
print(lista)

posortowane = []

while len(lista) != 0:
    element = lista[0]
    for i in lista:
        if i > element:
            pass
        elif i == element:
            pass
        else:
            element = i

    posortowane.append(element)
    lista.remove(element)

print(posortowane)

