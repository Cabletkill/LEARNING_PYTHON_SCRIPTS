receita = {'Jan': 100, 'Fev': 250, 'Mar': 400}
'''
receita = {'Jan': 100, 'Fev': 250, 'Mar': 400}
print(receita)
#Interar sobre Dicionario
for chave in receita:
    print(chave)
for chave in receita:
    print(receita[chave])
for chave in receita:
    print(f'Em {chave} o valor de R${receita[chave]},00.')
'''
'''
#Acessando a Chave do Dicionario
print(receita.keys())#demonstra a chave dentro do DIC!
for chave_de_acesso in receita.keys():# É recomendavel seguir sempre desta forma nesse tipo de caso!
    print(receita[chave_de_acesso])
'''
'''
#Acessando os valores do DIcionario
print(receita.values())
#desempacotamento de Dicionários
for chave_de_acesso, valor in receita.items():
    print(f'chave={chave_de_acesso} e valor={valor}')
'''

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))