def lista():
    lista = [2, 4, 2, 2, 3, 3, 1]
    return lista

def ordenada():
    x=sorted(lista())
    return x

def remove_repetidos():
    lista=ordenada()
    i = 0
    novalista = []
    for n in range(1, len(lista)):
        if i <= 0:
            novalista.append(lista[i])
        if lista[i] < lista[n]:
            novalista.append(lista[n])
        i = i + 1
    print(novalista)

remove_repetidos()