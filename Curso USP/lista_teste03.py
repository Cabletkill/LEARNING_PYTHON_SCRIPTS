ntpalavras=input("digite o texto:")
lista=ntpalavras.split()
#ntpalavras2=input("digite o texto:")
#lista02=ntpalavras2.split()

print('imprime o texto em forma de lista= ',lista)
print()
#print('imprime o texto em forma de lista = ', lista02)
conta = sorted(ntpalavras.split())
#conta02 =sorted(ntpalavras2.split())
print()
print(conta)
#print(conta02)
contagem = 0
tampalavras=0

contador=0
for i in range (len(ntpalavras.split())):
    for j in range (len(ntpalavras.split())):
        if conta[i]==conta[j]:
           contador = contador + 1
           print(i,conta[i],j,conta[j])
        else:
            contador = contador +0

i = 0
novalista = []
for n in range(1, len(ntpalavras.split())):
    if conta[i]==conta[j] :
       novalista.append(conta[i])
    if conta[i]==conta[j] :
        novalista.append(lista[n])
    i = i + 1

print('Relação = ',contador)
