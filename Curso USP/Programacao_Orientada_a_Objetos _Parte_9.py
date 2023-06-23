#def entrada():
 #   lista = [1, 3, 10, 110, 190, 330, 800]
  #  elemento = 3
   # busca(lista, elemento)

def busca(lista, elemento):
    for i in range(len(lista)):
        if elemento == lista[i]:
           return i
    return False



#entrada()
