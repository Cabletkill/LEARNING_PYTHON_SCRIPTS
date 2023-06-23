senha=int(input('Digite sua Senha:'))

x=2312
cont=1
while senha!=x and cont < 4:
    print('Senha Invalida!')
    print('Voce so tem mais', 4-cont,'tentativas')
    senha = int(input('Tente novamente: '))
    cont=cont+1

if senha == x:
   print('Acesso permitido!')
else:
   print('Numero de Tentativas Excedidas')