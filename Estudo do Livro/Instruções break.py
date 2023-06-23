def entrada_de_dados():
    nome = input('Digite seu nome: ')
    senha = int(input("Digiete sua Senha: "))
    compara_cadastro_nome(nome)
    compara_cadastro_senha(senha)
def senha_correta(senha):
    senha = 89801823
    return senha
def compara_cadastro_nome(nome):
    if nome == "Ricardo de Souza Silva":
       print("Nome encontrado!")
    else:
        while nome != "Ricardo de Souza Silva":
              print("Nome errado")
              nome = input('Digite Seu Nome Novamente: ')
def compara_cadastro_senha(senha):
    if senha == senha_correta(senha):
        print('Senha encontrada!')
    else:
         while senha != senha_correta(senha):
               print('Senha Errada')
               senha = int(input("Digite sua Senha Novamente: "))
entrada_de_dados()
print('Vamos fazer o pedido?')
resposta = input("")

if resposta.upper() == 'Sim':
    print('OK')

sys.exit()


