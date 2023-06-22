# DRY- dont repeat yourself? dont repeat you code:
'''
def contador():
    print('Parabens')
    print('Pra')
    print('voce')
print()
x=int(input('Quantas vezes voce vai repitir: '))
cont=0
#loop de repetição chamando a função:
for _ in range(0,x):
    contador()
    cont=cont+1
    print(cont)
'''
'''
numeros=[1,2,3,4,5,6,7,8,9,10]
ret=numeros.pop()
print(numeros)
print(f'Retorno de pop: {ret}')
'''
def quad7():
    y=int(input('DIgite o primeiro:'))
    return y

#print(f'Returno da função = {quad7()}')
x=int(input('Digite:'))
soma = quad7() // x
print(soma)
