def main():
   m1 = [[20, 3, 40], [5, 60, 7]]
   m2 = [[2, 3, 4], [5, 6, 7]]
   soma_matrizes(m1,m2)

def soma_matrizes(m1, m2):
    print(len(m1))
    print(len(m2))
    lista = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            a = m1[i]
            b = m2[i]
            nova_matriz = []
            for j in range(len(a)):
                # print(a[j]) #verificação de saidas A
                # print(b[j]) #verificação de saidas B
                # print(soma)
                soma = a[j] + b[j]
                nova_matriz.append(soma)
            lista.append(nova_matriz)
        print(lista)
        #return lista
    elif not len(m1) == len(m2):
        return False

main()


