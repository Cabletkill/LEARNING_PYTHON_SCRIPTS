#def main():
#    m1 = [[1], [4], [3]]
#    m2 = [[1, 2, 3]]
#    sao_multiplicaveis(m1, m2)

def sao_multiplicaveis(m1, m2):
    lista1 = []
    lista2 = []
    cont = 0
    for i in range(len(m1)): #separa a m1 e transforma em umna lista1
        a = m1[i]
        for y in range(len(a)):
            lista1.append(a[y])
    for i in range(len(m2)):#separa a m2 e transforma em umna lista2
        b = m2[i]
        for y in range(len(b)):
            lista2.append(b[y])

    for i in range(len(lista1)):# confere se a lista1 ea lista 2 são multiplos!!!
            a = lista1[i]
            b = lista2[i]
            if a % b == 0:
               cont = cont + 1
    if cont == len(lista1):
        print(True)
    else:
        print(False)
    #confere(cont, lista1)

#def confere(cont,lista1):
#    if cont == len(lista1):
#        print(True)
#    else:
#        print(False)

#main()


