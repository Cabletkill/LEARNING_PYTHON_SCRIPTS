''''
def entrada(num, pont=2): nesse caso se não houver parametro a funcao assume o 2 como padrao
    return num**pont

print('primeiro = ',entrada(2,3))
print('segundo = ',entrada(3,2))

print('terceiro =',entrada(2))#eleva ao quadrado
print('cuarto = ',entrada(2,3))
'''  #defaut
'''
def soma (n1,n2=8):
    return n1+n2
print(soma(1,2))
print(soma(98,2))
print(soma(9,10))
print(soma(18,))
'''  #exemplo01
'''
def mostra(nome='Ricardo', instructor=False):
    if nome=="Ricardo" and instructor:
        return "bem vindo, Ricardo"
    elif nome =="Ricardo":
        return "Eu não te conheço"
    return f'Ola {nome}'

print (mostra('Ricardo'))
print (mostra(nome='Ricardo'))
print (mostra('Ricardo', instructor=True))
''''



v = 1
def f():
   global v
print v