print('Bem-vindo ao jogo do NIM! Escolha:')
def computador_escolhe_jogada(m, n):
              if not n % (m + 1) == 0:
                     if not n % (m + 1) == 0 and n > m:
                            pcjoga = n - m // m
                            n = pcjoga
                            cont1 = 1
                            while not n % (m + 1) == 0 and n > m:
                                      pcjoga = n - m // m
                                      cont1 = cont1 + 1
                                      n = pcjoga
                            print("Computador tirou", cont1, "peça")
                     elif n == m:
                          print("Computador tirou", n, "peça")
                          pcjoga = n-m
                     else:
                         print("Computador tirou", n, "peça")
                         pcjoga = n - n
              return pcjoga   # recebe a jogada do computador e devolve
def usuario_escolhe_jogada(m,n):
       jogador2 = 0
       USUARIO = int(input('Quantas peças você vai tirar? '))
       if USUARIO > m:
          print()
          print('Oops! Jogada inválida! Tente de novo.')
          USUARIO = int(input('Quantas peças você vai tirar? '))
       n = n - USUARIO
       jogador2 = n
       print("Você tirou", USUARIO, "peça")
       print()
       return jogador2
def partida():
    n = int(input('Quantas peças?:'))
    m = int(input('Limite de peças por jogada?:'))
    while n<m:
          n = int(input('Quantas peças?:'))
          m = int(input('Limite de peças por jogada?:'))
    computador = False
    if n % (m + 1) == 0:
        print("Você começa!")
        print()
    elif not n % (m + 1) == 0:
         print('Computador começa!')
         print()
         computador=True
    while n > 0:
         #Entrada PC
          if computador:
             pcretira=computador_escolhe_jogada(m,n)
             n=pcretira
             if pcretira == 1:
                print()
             elif pcretira > 1:
                 print("Agora resta apenas", n, "peça no tabuleiro. ")
                 print()
             computador = False
          else:
             # entrada do Jogador
             jogador = usuario_escolhe_jogada(m, n)
             n = jogador
             if jogador == 1:
                 print()
             elif jogador > 1:
                 print()
                 print("Agora resta apenas", jogador, "peça no tabuleiro. ")
             computador = True
    if n == 0 or n < 0:
        print()
        print('Fim do jogo! O computador ganhou!')
def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')
print()
print("1 - Para jogada unica: ")
tipoDePartida = int(input('2 - para jogar um campeonato: '))

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
elif tipoDePartida == 1:
     print()
     print('Voce escolheu jogada unica!')
     print()
     partida()



