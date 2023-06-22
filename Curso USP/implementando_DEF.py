def partida(n,m):
    if n % (m) == 0:
       return True
    else:
       return False

def usuario_escolhe_jogada(m,n):
    while partida(m,n)==True:
          print("Usuario começa!")
          x=int(input('Quantas peças usuario vai tirar? N:'))
          n = n - x
          print('O usuario tirou', x, 'peça.')
          print('Agora restam', n, 'peças no tabuleiro..')
          while x > m :
                print('Jogada invalida, jogue novamente:')
                x= int(input('Quantas peças usuario vai tirar? N:'))
                n = n-x

def computador_escolhe_jogada(m,n):
    print("Computador começa!")
    while partida(m,n)==False:
          if   partida(m,n)==1:
               x=int(input('Quantas peças computador vai tirar? N:'))
               n = n - x
               print('O computador tirou',x,'peça.')
               print('Agora restam' ,n, 'peças no tabuleiro..')


def entrada():
    n=int(input('Quantas peças? N:'))
    m=int(input('Limite de peças por jogada? M:'))
    usuario_escolhe_jogada(m,n)
    computador_escolhe_jogada(m, n)

entrada()

