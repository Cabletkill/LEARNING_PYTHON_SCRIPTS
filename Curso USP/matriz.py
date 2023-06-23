def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []

        for j in range(num_colunas):
            valor = int(input('digite o elemento:[' + str(i) + '][' + str(j) + ']'))
            linha.append(valor)

        matriz.append(linha)

    return matriz


def lematriz():
    lin = int(input("Digite numeros de linhas: "))
    col = int(input('Digite numeros de colunas: '))
    return cria_matriz(lin, col)

