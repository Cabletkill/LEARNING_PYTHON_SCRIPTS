
spam = [
    'Coffee',
    'Orange',
    'Maçã'
]
nova = []
print(spam)
for i in range(len(spam)):
    lista = [
        "Maçã",
        "Orange",
        "Apple"
    ]
    for j in range(len(spam)):
        if lista[j]==spam[i]:
            nova.append(spam[i])
print(nova)
print()
print()
nome = "Ricardo"
#nome[2] ="R" #esse tipo de entrada gera erro
novo_nome = nome[4] + "the" + nome[1:7] # inclur corretamente
print(novo_nome)
print(nome)

eggs = [1,2,3]
print(eggs)
eggs = [4,5,6]
print(eggs)
eggs.append(eggs)
print(eggs)
