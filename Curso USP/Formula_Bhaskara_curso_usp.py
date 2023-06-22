import math
# import matplotlib.pyplot as plt


def delta(a, b, c):
    return (b ** 2) - 4 * a * c


def imprime_raizes(a, b, c):
    if delta(a, b, c) < 0:
        print('Delta menor que Zero')
    elif a == 0:
        print('Conta invalida')
    else:
        raiz1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        raiz2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
        print('Valor de delta =', delta(a, b, c))
        print(math.sqrt(delta(a, b, c)))
        print()
        print("Valor de X-I =", raiz1)
        print("Valor de X-II =", raiz2)
        print()
        print(f'Resultado fatoração A * (x - x¹) (x - x²) = {a} * (x - {raiz1}) (x - {raiz2})')
        # plt.scatter(raiz1,raiz2)
        # plt.show()


def main():
    a = float(input('Digite A: '))
    b = float(input('Digite B: '))
    c = float(input('Digite C: '))
    print()
    imprime_raizes(a, b, c)


main()
