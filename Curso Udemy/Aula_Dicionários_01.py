"""
Em outras linguagens o dicionario e conhecidos como mapas

Dicionarios => são coleções do tipo chave/valor.
[0,1,2]chave
[1,2,3]valor
Dicionario são representados por chaves{}
"""
#print(type({}))
# 1ºForma mais comum de se fazer um DIC
"""
paises = {'BR': "Brasil", "US": "Estados Unidos da America", 'PY': 'Paraguai'}#chave e valor são separados por :
print(paises)
print(type(paises))
"""
# 2º Forma
"""
paises = dict(BR="Brasil",US="Estados Unidos",PR="Paraguai")
print(paises)
print(type(paises))
"""
# Acessando elementos
# 1ºForma
"""
paises = dict(BR="Brasil",US="Estados Unidos",PR="Paraguai")
print(paises["BR"])
print(paises["US"])
#print(paises["B"])#KeyError: 'B' quando o elemento não existe
"""
# 2º Forma
"""
paises = dict(BR="Brasil",US="Estados Unidos",PR="Paraguai")
print(paises.get("BR"))#utilizando o .GET
"""
#Buscando a chave sem valor!!!!
"""
paises = {'BR': "Brasil", "US": "Estados Unidos da America", 'PY': 'Paraguai'}#chave e valor são separados por :
print('BR' in paises)# busca somente a chave não o valor
print('Estados Unidos' in paises)# nesse caso o valor não é reconhecido e o resultado e False
if "BR" in paises:
    Brasil = paises ["BR"]
    print(Brasil)
"""
#Dicionario utiliza qualquer tipo de dados
"""
localidade = {
    (35.685, 39.6917): "Escritorio de Tokio",
    (35.666, 39.6919): "Escritorio de Brasil",
    (35.667, 39.6920): "Escritorio de Estados Unidos"
}#tupla no dicionario
 
print(localidade)
"""
# Adicionar Elementos em um dicionario
'''
receita = {"Jan": 100,"Fev": 200, "Mar": 250}
print(receita)
#Forma 01
receita["Abri"] = 350 # incluindo um novo elemento no dicionario RECEITA
print(receita)
#Forma 02
novo_dado = {"Mai": 500}# incluindo um novo elemento no dicionario RECEITA
receita.update(novo_dado)# chamando a atualização na RECEITA
print(receita)
#Atualizando  dados em um dicionario
#Forma01
receita["Mai"] = 600 # chamando a atualização na RECEITA 
print(receita)
#Forma02
receita.update({"Mai": 700})# chamando a atualização na RECEITA
print(receita)
# Em dicionario NAO pode ter chave repitida
'''
#Remover dado de um dicionario
'''
receita = {"Jan": 100,"Fev": 200, "Mar": 250}
print(receita)
#FORMA 01
receita.pop('Jan')#Chamada de funcao que remove dados do dicionario
print(receita)
ret = receita.pop('Fev')# O valor removido retorna para o """"""ret"""""
print(ret)
print(receita)
#FORMA 02
receita = {"Jan": 100,"Fev": 200, "Mar": 250}

del receita["Fev"] #DELETA o elemento do dicionario/o valor removido não sera retornado
print(receita)
'''
#LISTA dentro do dicionario
'''
carrinho = []
produto1 = ["Playstation", 1, 5000]
produto2 = ["Xbox One", 1, 6000]
carrinho.append(produto2)
carrinho.append(produto1)
print(carrinho)
'''

