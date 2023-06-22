'''
Teste de ativo ou nao ativo com upper para deixar os caracteres iguais
'''


ativo=input('Voce esta ativo:')
logado=input('Voce esta ativo:')
ativo=ativo.upper()
logado=logado.upper()

if ativo=='SIM' and logado=="SIM":
    print('Bem vindo Usuário!')
else:
    print('Você precisa ativar sua conta. Por favor , cheque seu e-mail!')


