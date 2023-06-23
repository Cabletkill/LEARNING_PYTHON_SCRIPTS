def entrada():
    nome = input("Qual seu nome?:")
    altura = input("Qual sua altura?:")
    peso = input("Qual seu peso?:")
    idade = input('Qual sua idade?:')
    cor = input("Qual sua cor?:")
    saida(nome, altura, peso, idade, cor)

class Cadastro:
      def __init__( self, nome, altura, peso, idade, cor):
          self.nome = nome
          self.altura = altura
          self.peso   = peso
          self.idade  = idade
          self.cor    = cor

def saida(nome, altura, peso, idade, cor):
    pre_test = Cadastro(nome, altura, peso, idade, cor)
    print(pre_test.nome)
    print(pre_test.altura)
    print(pre_test.peso)
    print(pre_test.idade)
    print(pre_test.cor)
    print(pre_test)
entrada()





