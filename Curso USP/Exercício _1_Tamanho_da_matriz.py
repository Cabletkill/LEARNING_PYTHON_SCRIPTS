def ent():
    minha_matriz = [[1], [2], [3]]
    dimensoes(minha_matriz)
def dimensoes(minha_matriz):
    cont = 0
    cont2 = 0
    for i in range(len(minha_matriz)):
        cont = cont + 1
        nova = minha_matriz[i]
        for j in range(len(nova)):
            cont2 = cont2 + 1
    cont2 = cont2 // cont
    print(f'{cont}X{cont2}')
ent()