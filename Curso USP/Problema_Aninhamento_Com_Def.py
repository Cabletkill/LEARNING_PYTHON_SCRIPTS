def entrada():
    x = int(input("Digite o Numero:"))
    fatorial(x)
def fatorial(x):
    while x != 1:
          fatorial = 1
          while x > 1:
                fatorial=fatorial*x
                x = x-1
          print(fatorial)
entrada()


