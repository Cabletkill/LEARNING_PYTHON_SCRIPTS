'''
1º Tuplas são imutaveis ou seja cada operação em uma tupla gera uma nova tupla
2º Listas são mutaveis podendo mudar costantemente
'''

lista =  tuple(range(20))# a tupla gera um range.
print(lista)
print()
print(max(lista))
print(sum(lista))
print(min(lista))
print()

tupla = ("Ricardo","Silva")
escola, curso = tupla  # desempacotamneto de tuplas
print(escola)
print(curso)
print(lista+tupla)
print(sorted(tupla))

lista02 = [1,2,3,4,5,6,8,9,10,11,20,50,1]
for i in lista02:
    print(i)
print('maximo',max(lista02))
print('soma',sum(lista02))
print('minimo',min(lista02))

g=list('Ricardo de Souza Silva')

print(sorted(g))