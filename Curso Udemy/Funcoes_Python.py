'''
Definindo Funções:
- Funções são peguenos trexos de codigo que realiza tarefas expecificas.
-Podendo ser em blocos.
'''
'''
cores=['verde','vermelho','amarelo','azul', 'branco']
#Utilizando a funçao integrada (Built-in) do Python print()
print(cores)
curso ='Programção am Pythom : Essencial'
print(curso)

cores.append('Roxo')
print(cores)
cores.clear()
print(cores)
'''
# DRY- dont repeat yourself? dont repeat you code:
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


