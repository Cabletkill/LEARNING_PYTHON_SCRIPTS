def main():
    x=int(input('Digite o numero da Tabuada:'))

    soma(x)
def soma(x):
    soma = 0
    for i in range(1,5+1):
        soma = soma + x
        x=x+2
        print('SOMA =', soma,i)


main()


