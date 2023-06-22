def eprimo(x):
         cont = 0
         while not cont == 2:
            for c in range(1, x + 1):
                  if x % c == 0:
                     cont = cont+1
            if cont <= 2:
                 return x
            elif cont >= 3:
                 return x-1
x = int(input("digite o numero:"))


print(eprimo(x))


