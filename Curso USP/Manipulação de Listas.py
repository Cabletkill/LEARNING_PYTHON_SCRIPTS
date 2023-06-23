#fatia de listas
'''
lista=[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
print(len(lista))
print(lista[1:7])
print(lista[3:10])
print(lista[0:10])
print(lista[10:18])

novalista=lista[12:]
print(novalista)
novalista.append(lista)
print(novalista)
'''    #lista de estudo

#Clone de lista
'''
lista=[123456789,123,456,789,987,654,321,147,852,369]
def clone(lista):
    clone=[]
    for objeto in lista:
        clone.append(objeto)
    return clone
print(clone(lista))
print(lista[:])
'''  #clonando listas

'''
lista01=['Ricardo','Michele','Samuel']
lista02=lista01[:]
lista02[0]='Livia'

print(lista02)

print('Livia' in lista01)
print('Livia' in lista02)

if 'Livia' in lista01:
    print('Esta na lista 01')
if 'Livia' in lista02:
    print('Esta na lista 02')

nova = lista01+lista02+[1,2,3,456,789,4,5,6]# concatenando lista
print(nova)

lista01.append(nova)#adicionando a lista
print(lista01)

del lista01[0:2]#Apagando itens da lista
print(lista01)
'''
'''
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes
carnes2.append("ponta de alcatra")

print(carnes)
print(carnes2)
'''
'''
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = []
for cns in carnes:
    carnes2.append(cns)
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2)
'''
'''
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes[:]
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2)
'''''

"""
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
if "ponta de alcatra" in carnes:
    print("XXX")
else:
    if "ponta de alcatra" in carnes2:
        print("YYY")
    else:
        print("ZZZ")
"""

carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1
print(carnes1)
print(carnes2)
print(carnes3)

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
x = carnes
del (x[-1])
print(carnes)
print(x)