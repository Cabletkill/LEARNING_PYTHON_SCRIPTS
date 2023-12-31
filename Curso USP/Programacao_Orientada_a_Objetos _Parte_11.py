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
            return lista

    def busca(self,lista):
        fim = len(lista)
        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1],  lista[j]
                if sorted(lista) != lista:
                    print(lista)


def bubble_sort(lista):
    o = Ordenador()
    o.selecao_direta(lista)


