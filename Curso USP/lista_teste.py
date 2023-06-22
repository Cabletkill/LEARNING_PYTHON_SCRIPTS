#Adiciona a lista:
lista = [2, 4, 2, 2, 3, 3, 1]
##list.sort() coloca a lista em ordem crecente
lista=sorted(lista)
i=0
s=[]
#remove_repetidos(lista)
for n in range (1, len(lista)):
    ##print('Teste de Lista N =',lista[n])
    novalista = []
    if lista[i]<lista[n]:
       print('lista = ', lista[i])
       if (n+1)==len(lista):
           print('lista = ', lista[n])
       list = [lista[i]]
       s.append(list)
    else:
        print(s)
    i = i + 1







#remove_repetidos([1, 2, 3, 3, 3, 4])
