s = set({1, 2, 3, 4, 5, 6, 7, 2, 4, 3, 8})
print(s)
c = {1, 2, 3, 4, 5, 6, 7, 2, 4, 3, 8}
print(c)
print(type(c))

tipo = set('Ricarod de souza Silva')
print(tipo)

if 2 in c:
    print('Ok')
else:
    print('not Ok')

print()

lista = [1, 2, 3, 4, 5, 6, 7, 2, 4, 3, 8]
print('lista', lista)
tupla = (1, 2, 3, 4, 5, 6, 7, 2, 4, 3, 8)
print('tupla', tupla)
dicionario = {}.fromkeys([1, 2, 3, 4, 5, 6, 7, 2, 4, 3, 8], 'dict' )
print(dicionario)