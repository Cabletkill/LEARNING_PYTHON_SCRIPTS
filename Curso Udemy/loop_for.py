'''
#exemplo de for 01
for letra in nome:
    print(letra)

#Exemplo FOR 02
for numero in lista:
    print(numero)

'''
'''
#Exemplo de FOR 03
range (valor_inicial, Valor_final)
Exemplo de 1 a 10 
Imprime:1,2,3,4,5,6,7,8,9 - (10)não

'''
'''
for numero in range(1,10) :
    print(numero)
'''
'''
enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2])
 ((0,'R'), (1, 'i'), (2,'c'), (3,'a'), (4,'r'), (5,'d'),(6,'o')...
for i, v in enumerate(nome):
    print(nome[i]) 
 
'''
'''
for _, letra in enumerate(nome):
    soma =soma +1
    print('[',soma,'][',letra,']')
    
no FOR 
quando não precisamos de um valor, nos descartamos o valor utilizando (_) underline


nome="Ricardo de Souza Silva"
lista=[1,3,5,7,9]
numeros=range(1,10)

for letra in enumerate(nome):
    print(letra)
'''
'''

qtd=int(input('Quantas vezes deve rolar:'))
soma =0
for n in range(1, qtd+1):
    num=int(input(f'Informe o {n} / {qtd}:'))
    soma =soma+num
print (f'A Soma é {soma}')
    
'''
'''
nome="Ricardo de Souza Silva"

for letra in nome :
    print(letra, end='')
'''
#original : U+1F60D
#modificado: U0001F60D

emoji='U0001F60D'
for _ in range (3):
    for num in range(1, 11):
        print('\U0001F70D'*num)



