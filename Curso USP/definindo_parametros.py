print('Bem-vindo ao jogo do NIM! Escolha:')
def eprimo(k,x):
    cont = 0
    for _ in range(1, k + 1):
        if k % (x+1) == 0:
            cont = cont + 1
    if cont <= 2:
        return k
    elif cont >= 3:
        return k
def maior_primo(k,x):
    while eprimo(k,x)==True:
          m = int(input('Jogador Quantas peças você vai tirar?'))
          k=k-m
          while m>x:
                k=k+m
                print(k)
                print('Oops! Jogada inválida! Tente de novo.')
                m = int(input('Jogador Quantas peças você vai tirar?'))
                k = k - m
          print('Você tirou',eprimo(k,x),'peça.', )
          print('Agora resta apenas',eprimo(k,x),'peça no tabuleiro.')
    return k
def maior2_primo(k,x):
    while eprimo(k,x)==False:
          m = int(input('Maquina Quantas peças você vai tirar?'))
          k=k-m
          while m>x:
                k=k+m
                print(k)
                print('Oops! Jogada inválida! Tente de novo.')
                m = int(input('Maquina Quantas peças você vai tirar?'))
                k = k - m
          print('Você tirou',eprimo(k,x),'peça.', )
          print('Agora resta apenas',eprimo(k,x),'peça no tabuleiro.')
    return k

def partida(): # entrada da variavel
    k=int(input('Quantas peças?'))
    x=int(input('Limite de peças por jogada?'))
    maior2_primo(k, x)
    maior_primo(k, x)
partida()

