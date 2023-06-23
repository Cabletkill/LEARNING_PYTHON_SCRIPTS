def main():
    number  = int(input("Digite o Numero: "))
    Collatz(number)
def Collatz(number):
    if number % 2 == 0:
        print(number // 2)
    elif number % 2 != 0:
          print(number * 3 + 1)

main()
