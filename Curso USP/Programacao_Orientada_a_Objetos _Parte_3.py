x =input("digite o nome do Cliente:")
y = input("digite a Idade:")
z = input('Digite a cor:')
a = input("Digite o sexo:")
b = input("Digite a Situação:")

class Cliente:
    def __init__(self, nome, idade, cor, sexo, situacao):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.sexo = sexo
        self.situacao = situacao
prospect_cliente = Cliente( x, y, z, a, b)


print(prospect_cliente.nome)
print(prospect_cliente.idade)
print(prospect_cliente.cor)
print(prospect_cliente.sexo)
print(prospect_cliente.situacao)

