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

def entrada():
    lista = [10, -20, 50, 10, 200, 33, -80]

    ordenada(lista)
def ordenada(lista):
    o = Ordenador()
    o.selecao_direta(lista)
    print(lista)
entrada()