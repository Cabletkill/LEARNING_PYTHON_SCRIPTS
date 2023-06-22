'''

def quadrado (numero):
    ##return numero * numero
    return numero **2
print(quadrado(11))
print(quadrado(2))
print(quadrado(5))

retorno = quadrado(10)
print(retorno)
print(quadrado())#type error
''' #funcao com retorno
'''
def cantar_parabens(aniver):
    print("Parabens pra Voce")
    print("Nesta data querida")
    print("Muitas felicidade")
    print(f'Viva o {aniver}!')

x='Ricardo'
cantar_parabens(x)
#print(cantar_parabens(x))#None
'''#funcao com retorno 02
'''
def soma (a,b):
    return a+b

def multiplica(num1,num2):
    return num1*num2

def outra(num1, b , msg):
    return (num1+b) * msg
print(soma(5,2))
print(soma(10,20))

print(multiplica(4,5))
print(multiplica(2,8))

print(outra(3,2, 'Geek'))
'''#funcao com retorno 03

#nomeando Parâmetros
#ParÂmetros são variaveis declaradas na definação de uma função
#Argumentos são dados passados durante a execução de uma função
#A Ordem dos parametros importa
#Argumentos nomeados (Keyboard Arguments)
''''
def nome_completo(Nome,Sobrenome):
    return f'Seu nome completo é {Nome} {Sobrenome}.'
print (nome_completo('Ricardo', 'Souza'))
print(nome_completo(Nome ='Angelina', Sobrenome='Jolie'))
print(nome_completo(Nome = Nome , Sobrenome = Sobrenome))
'''

#Erro  comum na Utilização do return

def soma (numero):
    total=0
    for num in numero:
        if num % 2!=0:
            total=total+num
    return total

lista =[1,2,3,4,5,6,7]
print(soma(lista))
