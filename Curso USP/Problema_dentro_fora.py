n = int(input('Quantas peças?:'))
m = int(input('Limite de peças por jogada?:'))
if n%(m+1)==0:
   print("Você começa!")
   print()
else:
   print('Computador começa!')
   print()

while n>0:
    if n % (m + 1) == 0:
       x=int(input('Quantas peças USUARIO vai tirar?:'))
       if x>m:
          print('Oops! Jogada inválida! Tente de novo.')
          x = int(input('Quantas peças USUARIO vai tirar?:'))
       n = n - x
       print()
       print("Você tirou",x,"peça")
       print("Agora resta apenas",n,"peça no tabuleiro. ")
       print()
    if not n % (m + 1) == 0:
       print()
       if n > m:
          print("Computador tirou", m, "peça")
          n=n - m
       elif n == m:
            print("Computador tirou", n, "peça")
            n=m - m
       elif n < m:
            print("Computador tirou", n, "peça")
            n = n - n
       print()
       if n==0:
          print('Fim do jogo! O computador ganhou!')
       else:
          print("Agora resta apenas", n, "peça no tabuleiro.")
          print()
