import random
import time
import
class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000)#inteiro entre 0 e 999
        return lista
    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista[:]

        o = Programacao_Orientada_a_Objetos_parte11.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print(depois-antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(depois - antes)

