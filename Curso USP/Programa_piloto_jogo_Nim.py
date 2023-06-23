print('Bem-vindo ao jogo do NIM! Escolha:')
print()
n = int(input('Quantas peças?:'))
m = int(input('Limite de peças por jogada?:'))
if n%(m+1)==0:
   print("Você começa!")
   print()
elif not n%(m+1)==0:
         print('Computador começa!')
         print()
while n>0:
      #entrada do Jogador
      if n % (m + 1) == 0:
         x=0
         x=int(input('Quantas peças USUARIO vai tirar?:'))
         if x>m:
            print('Oops! Jogada inválida! Tente de novo.')
            x = int(input('Quantas peças USUARIO vai tirar?:'))
            n = n - x
            print()
            print("Você tirou",x,"peça")
            print("Agora resta apenas",n,"peça no tabuleiro. ")
            print()
      #entrada do PC
      if not n % (m + 1) == 0:
             print()
             if not n % (m + 1) == 0 and n > m:
                    n = n - m // m
                    cont1=1
                    if not n % (m + 1) == 0 and n > m:
                           n = n - m // m
                           cont1=cont1+1
                    print("Computador tirou",cont1 , "peça")
             else:
                  print("Computador tirou", n, "peça")
                  n=n-m
                  print()
             if n==0:
                print('Fim do jogo! O computador ganhou!')
             elif n>0:
                  print("Agora resta apenas", n, "peça no tabuleiro.")
                  print()
             else:
                 print("Fim do jogo! O computador ganhou!")
                 print()
