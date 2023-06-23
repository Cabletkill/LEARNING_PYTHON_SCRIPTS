def main():

    import math

    a=float(input('Digite A: '))
    b=float(input('Digite B: '))
    c=float(input('Digite C: '))


    delta = (b**2)-4*(a)*(c)
    print(delta)

    if delta < 0:
      print('Delta menor que Zero')
    elif a==0:
        print('Conta invalida')
    else:
         raiz1= (-b + math.sqrt(delta))/(2*a)
         raiz2 = (-b - math.sqrt(delta)) / (2 * a)
         print(raiz1)
         print(raiz2)

    ###primeira parte da resoluçao delta X1
    #p1 = -(b)
    #p2 = delta
    #p3 = (2 * a)
    #x= p1+p2
    #y=p3
    #y1=x / y
    #print(y1)
    ###segunda parte da resolução delta X2
    #p1 = -(b)
    #p2 = delta
    #p3 = (2 * a)
    #x = p1 - p2
    #y = p3
    #x2 = x / y
    #print(x2)

         if raiz1 > 0 and raiz2 > 0:
            print('Resultado: Q1')
         elif raiz1 > 0 and raiz2 < 0:
            print('Resultado: Q2')
         elif raiz1 < 0 and raiz2 < 0:
            print('Resultado: Q3')
         elif raiz1 < 0 and raiz2 > 0:
            print('Resultado: Q4')
         else:
            print('Resultado: X')
main()