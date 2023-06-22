'''
def diz_oi():
    return 'ola'

x=' Ricardo'

print(diz_oi() + x)

Exemlo: 1 Return finaliza a função, ou seja ele sai da função

def diz():
    print('estou antes do return ')
    return ' ola '
    print('estou apos o return ')

print(diz())

exemplo:2 Podemos ter em uma função varios Returns
def nova():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return "b"
print(nova())

exemplo 3 Podemos em uma função retornar qualquer tipo de dado ate mesmo multiplos valores
def outro():
    return 2,3,4,5
#n1,n2,n3,n4=outro()
#print(n1,n2,n3,n4)
print(outro())

'''
#Vamos criar uma função para car ou coroa
from random import random
def jogada():
    #Gera um numero pseudo randomico entre 0 e 1
    if random() > 0.5:
        return 'cara'
    return 'coroa'
print(random())
print(jogada())

"""
Erros na utilização do return e codificação desnecessaria
"""
def impar():
    numero=50
    if numero%2!=0:
       return True
    return False
print(impar())