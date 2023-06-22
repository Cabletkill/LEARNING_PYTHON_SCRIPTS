def main():

    import math

    x1=float(input('Digite x1: '))
    x2=float(input('Digite x2: '))
    y1=float(input('Digite y1: '))
    y2=float(input('Digite y2: '))

    distancia=((x1-x2)**2)+((y1-y2)**2)
    raiz=math.sqrt(distancia)
    if raiz >= 10:
        print('longe')
    else:
        print('perto')


main()