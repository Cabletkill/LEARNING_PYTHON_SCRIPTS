""""
Programação orientada  a objetos::::
Objeto: dados + código
- encapsulamento

Classes:
Definem os tipos de objetivos
Definem quais os dados e o codigo dos objetos

Dados => Atributos
Codigo => metodos
Os objetos são chamados de instancias das classes

classe = Carro
instancias: meu_carro, carro_do_ime
Atribudos:
ano, modelo, cor e variedade
Metodos:
acelera(velocidade)
pare()
"""
class Carro:
    pass
meu_carro = Carro()
#print(meu_carro)
carro_do_ime = Carro()
#print(carro_do_ime)
meu_carro.ano = 1968
meu_carro.modelo = 'Fusca'
meu_carro.cor = 'Azul'

carro_do_ime.ano = 1983
carro_do_ime.modelo = 'porshe'
carro_do_ime.cor = 'branco'




