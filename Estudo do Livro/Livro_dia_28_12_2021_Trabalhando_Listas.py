lista_animais = []
quantidade_de_gatos = int(input('Quantos gatos voce quer listar?'))

while quantidade_de_gatos > 0:
    quantidade_de_gatos = quantidade_de_gatos - 1
    nomes_dos_gatos = input("Digite o nome do gato!")
    lista_animais.append(nomes_dos_gatos)
print(lista_animais)
#Primeiro programa de lista de nomes dos gatos


