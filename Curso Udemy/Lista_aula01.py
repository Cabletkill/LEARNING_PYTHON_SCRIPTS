''''
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem Dinâmico e Tambem podemos colocar Qualquer tipo de dado.

Em python:
Dinámico: Não possui tamanho fixo; ou seja podemos criar a lista e simplismente ir adicionando elementos;
Qualquer tipo de dado: As listas não possuem tipo de dado; fixo ou seja, podemos colocar qualquer tipo de dado.
Lista em python são representadas por colchetes[]
'''
lista=[1,2,3,4,10,8,7,8,99,10,121,12,213,14,3315,16,15617,18,15559,20,21,22,23,24,25,26,27,28,29,30 ]
lista2=['a','A','B','b','cC','D','E','e']
lista3=[]
lista04= list(range(11))
lista05=list('Ricardo')
print(lista05)
#Podemos facilmente checar se determinado valor esta contido na lista
num =11
if num in lista:
    print(f"Encontrei {num}")
else:
    print(f'Não encontrei {num}')
print(lista2)
dir(lista)
print(dir())
#Podemos ordenar a lista
lista2.sort()
print(lista2)
#podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista.count(10))
print()
#podemos adicionar elementos em listas
'''
Para adicionar elementos ou valores em lista usamos a função append.
OBS: Com append nos so conseguimos adicionar um elemento por vez
'''
print(lista)
lista.append(42+20)
print(lista)
#lista.append(42,20,20)#Erro
lista.append([1,2,3,4,5,1,3,56])
print(lista)
if [1,2,3,4,5,1,3,56] in lista:
    print(f'Encontrei a lista {[1,2,3,4,5,1,3,56]}')
else:
    print(f'Não encontrei a lista{[1,2,3,4,5,1,3,56]}')

lista.extend([123,44,64])

print(lista)