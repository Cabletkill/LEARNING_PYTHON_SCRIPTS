def entrada ():
    x= int(input("Quantos numeros voce vai digitar?:"))
    y = 0
    q = 0
    lista = []
    conta(x,y,q,lista)

def conta(x,y,q,lista):
    while x > y:
          numero = int(input('Digite o numero: '))
          y = y + 1 # serve como contador
          if numero % 2 == 0:
             lista.append(numero)# recebe o numero par e devolve em uma lista
             q = q + 1
   emprime(q,lista) #seguindo o fluxo com a chamada de func

def emprime (q,lista):
    print("numeros pares : ", lista)
    print('Quantidade de pares', q)


entrada()