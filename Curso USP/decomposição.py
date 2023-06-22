n = int(input("Digite um numero: "))
anterior = n % 10
n = n // 10;
posterior_iguais = False;
pos = 0

while n > 0 and not posterior_iguais:
      atual = n % 10
      if atual == anterior:
         posterior_iguais = True
      else:
         pos += 1
      anterior = atual
      n = n // 10

if posterior_iguais:
    print("sim", atual)
else:
    print('não')