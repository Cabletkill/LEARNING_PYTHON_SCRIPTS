class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
carro_do_meu_avo = Carro('Ferrari', 1983, 'Vermelho')
#print(carro_do_meu_avo.cor)
#print(carro_do_meu_avo.modelo)
#print(carro_do_meu_avo.ano)

class Lista:
    def append(self, elemento):
        return "Oops! Este objeto não é uma lista"
lista = []

a = Lista()
b = a.append(7)
lista.append(b)
print(lista,a,b)

class Cachorro:
    def __init__(self, raça, idade, nome, cor):
        self.raça = raça
        self.idade = idade
        self.nome = nome
        self.cor = cor


rex = Cachorro('vira-lata', 2, 'Bobby', 'marrom')

#print(rex.cor)
#print(rex.raça)
#print(rex.nome)
#print(rex.idade)