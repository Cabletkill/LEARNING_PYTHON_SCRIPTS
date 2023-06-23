from random import randint

n1 = randint(1, 60)
n2 = randint(1, 60)
lista = []
for i in range(1, 7):
    lista.append(n1)
    if n1 == n2:
       n2 =- 5
    else:
        n1 = randint(1, 60)

print(sorted(lista))