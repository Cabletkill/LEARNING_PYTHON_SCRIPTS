import random as aleatorio

print("Tente advinhar um Numero.")
print()
def entrada():
    x = int(input("Quantas vez voce vai arriscar?:"))
    jogada(x)
def jogada(x):
    for i in range(1,x+1):
        secret_number = aleatorio.randint(1,100)
        number = int(input("Qual sera o numero?:"))
        teste_jogada(secret_number, number)
def teste_jogada(secret_number, number):
        j = 0
        if number == secret_number:
            j = j + 1
            print("Voce acertou")
            print(f'Voce ganhou {j} pontos')
            print()
        else:
            print('Voce errou')
            print(f'O numero correto é {secret_number}')
            print()

entrada()
