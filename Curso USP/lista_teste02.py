ntpalavras=input("digite o texto:")
lista=ntpalavras.split()
#ntpalavras2=input("digite o texto:")
#lista02=ntpalavras2.split()

print('imprime o texto em forma de lista= ',lista)

#print('imprime o texto em forma de lista = ', lista02)
conta = sorted(ntpalavras)
ct=lista.sort()
print
#print(conta)
#conta02 =sorted(ntpalavras2)

print(conta[0])
contagem = 0
tampalavras=0
iguais = 0
diferentes = 0
for i in range (len(ntpalavras)):
    if conta[i] == ' ' or conta[i] == ',' or conta[i] == '.' or conta[i] == ';' or conta[i] == ':':
        contagem = contagem + 1
    else:
        tampalavras = tampalavras + 1

print('Total de Caracteres:',len(conta))
print()
print("total de Letras",tampalavras)
print()
print('Total de virgulas, pontos e espaços',contagem)
print()
print('Total de Palavras ',len(ntpalavras.split()))
print()
tamanhomediodepalavra = tampalavras/len(ntpalavras.split())
print('Tamanho medio da palavra',tamanhomediodepalavra)

