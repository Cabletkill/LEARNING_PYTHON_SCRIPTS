

def quadrante():
    if x > 0 and y > 0 :
        print('QUADRANTE Q1')
    elif x > 0 and y < 0:
        print('QUADRANTE Q2')
    elif x < 0 and y < 0:
        print('QUADRANTE Q3')
    elif x < 0 and y > 0:
        print('QUADRANTE Q3')
    elif x==0 and y==0:
        print('Eixo 0')

x = int(input('Digito o x= '))
y = int(input('Digite o y= '))




