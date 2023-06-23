def entrada():# first of all you need the quantity of parameter that you will analyzes
    x=int(input('Quantos numeros serao digitados?:'))
    cont(x)

def cont(x):#here the func recive the parameter and return position
    lista = []
    cont = 0
    contador = 0
    for i in range (1, x+1):
        j=int(input('Digite um numero: '))
        lista.append(j)
        if j > cont:
           cont = j
           contador = i
    printa(lista, contador)

def printa(lista,contador):# this part print the list of cont (x)
    print()
    print('MAIOR VALOR =',max(lista))
    print()
    print('POSICAO DO MAIOR VALOR =',contador)
entrada()



