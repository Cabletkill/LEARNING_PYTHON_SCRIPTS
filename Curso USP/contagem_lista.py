from typing import List, Any

lista = [6, 7, 8, 3, 10, 19, 4, 1, 0, 61, 30, 16, 17, 82, 29, 34, 43, 21, 11, 39, 56, 67, 12]
x = sorted(lista)


def remove_repetidos(x):
    lista_nova: object = x
    i = 0
    novalista: list[Any] = []
    for n in range(1, len(lista_nova)):
        if i <= 0:
            novalista.append(lista_nova[i])
        if lista_nova[i] < lista_nova[n]:
            novalista.append(lista_nova[n])
        i = i + 1
    return novalista


print(remove_repetidos(x))






