
n = int(input('Quantas peças?:'))
m = int(input('Limite de peças por jogada?:'))
while n>0:
      if n % (m + 1) == 0:
         x=0
         x=int(input('Quantas peças USUARIO vai tirar?:'))
         if x>m:
            print('Oops! Jogada inválida! Tente de novo.')
            x = int(input('Quantas peças USUARIO vai tirar?:'))
         n = n - x
      if not n % (m + 1) == 0:
             print()
             cont=0
             if not n % (m + 1) == 0 and n > m:
                 for i in range (0,m+1):
                     if not n % (m + 1) == 0 and n > m:
                            cont = cont + 1
                 if cont >=1:
                    if cont < m:
                       n=n-cont
                       print("Computador tirou", cont, "peça")
                    elif cont > m:
                         n=n-m
                         print("Computador t", m, "peça")
