carrinho = []
produto = ''

while produto != 'sair': # comando que adiciona enquanto não for 'SAIR"
      print('Adicione um produto na lista ou digite  "sair" para sair.')
      produto = input()
      if produto != 'sair':
         carrinho.append(produto)

for produto in carrinho:# print todos os produtos da lista
    print(produto)
