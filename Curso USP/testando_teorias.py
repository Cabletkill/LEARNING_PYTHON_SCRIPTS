def entrada(): # entrada da variavel
    x=int(input('Digite o Valor de X:'))
    y= int(input('Digite o Valor de Y:'))

    maior_primo(x,y)
    maior_primo2(x,y)

def eprimo(x,y):
    if x % (y+1) == 0:
       return True
    elif not x % y == 0:
       return False

def maior_primo(x,y):

    while eprimo(x,y)==True:
          m= int(input('Digite o Valor de K:'))
          x=x-m
    print("Teste Primeiro Resultado =",x)
    ##return k
def maior_primo2(x,y):

    while eprimo(x,y)==False:
          m= int(input('Digite o Valor de K:'))
          x=x-m
    print("Teste Segundo Resultado =",x)
    ##return k


entrada()