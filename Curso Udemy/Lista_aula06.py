lista=[1,2,3,4,10,8,7,8,99,10,121,12,213,14,3315,16,15617,18,15559,20,21,22,23,24,25,26,27,28,29,30 ]

slice = lista [5:] # corta e retira o numero
print(list(enumerate(lista)))#cria um numerador da lista
print()
print(slice)
print()
slice = lista [:6] # corta e retira o numero
print(slice)
print()
print (lista [ 1 : 10+1 ]) # lista pode ter [inicio : fim : passo que]
print()
print(lista[1:: 2])# lista segue de 2 em 2
print()
print(lista[:: -1])
print()
print(sorted(lista[1::-1]))

print(sum(lista))
print(max(lista))
print(min(lista))

#lista vira tupla
tupla = tuple(lista)
print(tupla)
print(type(tupla))

