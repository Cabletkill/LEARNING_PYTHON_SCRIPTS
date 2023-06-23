class Ordenador:

    def selecao_direta(self, lista):
        fim =len(lista)
        for i in range(fim-1):
            #Inicialmente, o menor elemento já visto é o I-ésimo
            posicao_do_minimo = i
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            #Coloca o menor elemento encontrado no início da sub lista
            # Para isso, troca de lugar os elementos nas posições I e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

#def entrada():

lista = [6, 7, 8, 3, 10, 19, 4, 1, 0, 61, 30, 16, 17, 82, 29, 34, 43, 21, 11, 39, 56, 67, 12]

    #bubble_sort(lista)
def bubble_sort(lista):
    fim = len(lista)
    for i in range(fim - 1, 0, -1):
        lista01 = []
        for j in range(i):
            if lista[j] > lista[j+1]:
               lista[j], lista[j+1] = lista[j+1],  lista[j]
               lista01 = lista
               print(lista01)
o = Ordenador()
o.selecao_direta(lista)
print(lista)

#entrada()