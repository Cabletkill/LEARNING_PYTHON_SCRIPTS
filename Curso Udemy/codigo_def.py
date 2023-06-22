def primeiro(x,y):
    x=x%(y)
    print(x)
    return x

def returno(x,y):
    if not primeiro(x,y)==0:
          x = int(input('Digite o returno Valor de X:'))
          x=x-1
    resenha(x,y)

def resenha(x,y):
    if primeiro(x,y)==0:
          x = int(input('Digite o resenha Valor de X:'))
          x=x-1
    returno(x,y)

def entrada():
    x=int(input('Digite o Valor de X:'))
    y=int(input('Digite o valor de Y:'))


entrada()
''''
teste de condição def com returno
'''