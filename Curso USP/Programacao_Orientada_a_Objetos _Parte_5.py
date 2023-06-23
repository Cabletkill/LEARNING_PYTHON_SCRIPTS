class Carro:
    pass

# teste da classe Carro
Fusca = Carro()
Brasilia = Carro()

#print(Fusca) # referencia da Memoria
#print(Brasilia) # referencia da Memoria
Fusca.ano = 1968
Fusca.modelo = "Fusca"
Fusca.cor = "Amarelo"

Brasilia.ano = 2010
Brasilia.modelo = "Brasilia"
Brasilia.cor = "Branca"

novo_fusca = Fusca
print("Fusca igual a brasilia? > ", Fusca == Brasilia)
print("Fusca igual o Novo Carro? >",Fusca == novo_fusca)
Fusca.ano += 10
print("Ano do Fusca = ", Fusca.ano)
print("Ano Novo Fusca", novo_fusca.ano)


