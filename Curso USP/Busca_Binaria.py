def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
          meio = (primeiro+ultimo)//2
          print(meio)
          if lista[meio] == elemento:
             print(meio)
             return meio
          else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
          if lista[meio] != elemento:
             print(meio)
    return False






lista = [1, 2, 3, 4, 5,6]

#lista = (['a', 'e', 'i'])
#print(busca(lista,4))
