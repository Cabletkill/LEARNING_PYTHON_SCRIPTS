X =(input('Voce vai digitar a temperatura em qual escala (C/F)? '))
soma:int
if X == ('C') or ('c'):
   Y=int(input('Digite a temperatura em Celsius: '))
   soma= Y * 1.8 + 32
   print('Temperatura equivalente em Fahrenheit: ',soma)
elif X == ("F") or ('f'):
     Y=int(input('Digite a temperatura em Fahrenheit: '))
     soma = (Y-32) / 1.8
     print(f'Temperatura equivalente em Celsius: ',soma)
    