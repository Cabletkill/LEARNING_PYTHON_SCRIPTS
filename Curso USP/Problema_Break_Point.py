'''
saindo do loop com break
utilizamos o break para sair de loops de maneira forçada ou de maneira projetada.
'''
##Exemplo 01

for numero in range (1,11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')
##Exemplo 02

while True:
    comando=input("digite sair para sair:")
    if comando == 'sair':
       break