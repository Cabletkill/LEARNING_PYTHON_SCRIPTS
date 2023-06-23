n=int(input("Digite um nume inteiro maior que 1:"))
fator  = 2
multp = 0
while n > 1:
    while n % fator == 0:
          multp = multp + 1
          n = n / fator
    if multp>0:
       print('Fator ', fator, 'Multiolicidade = ', multp)
    fator  = fator + 1
    multp = 0