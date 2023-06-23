x = int(input('Qual numero voce vai decompor?:'))

fator=2
multiplicidade = 0
cont = 0

while not x==1:
    while x%fator==0:
        multiplicidade=multiplicidade+1
        x = x / fator
        while not cont == 2:
            for c in range(1, x + 1):
                if x % c == 0:
                    cont = cont + 1
            if cont <= 2:
                print('Primo')
            elif cont >= 3:
                print('Não é primo')
    if multiplicidade>0:
            print ('Fator', fator, 'multiplicidade =', multiplicidade)
    fator = fator + 1
    multiplicidade=0

