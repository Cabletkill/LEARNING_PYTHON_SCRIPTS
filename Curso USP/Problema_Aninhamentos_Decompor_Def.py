x = int(input('Qual numero voce vai decompor?:'))

fator=2
multiplicidade = 0
while not x==1:
    while x%fator==0:
        multiplicidade=multiplicidade+1
        x = x / fator
    if multiplicidade>0:
            print ('Fator', fator, 'multiplicidade =', multiplicidade)
    fator = fator + 1
    multiplicidade=0
