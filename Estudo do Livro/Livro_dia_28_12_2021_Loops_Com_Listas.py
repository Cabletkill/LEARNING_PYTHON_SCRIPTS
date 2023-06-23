"""
lista = []
for i in range(0,10+1,2):
    lista.append(i)
print(lista)
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str (i) + ' in supplies is: ' + supplies[i])

print('pens' in supplies) #verificador de conteudo dentro de uma lista
print('pes' in supplies)
"""
"""
myPets = ['Marcos', 'Helena', 'Gaspar', 'Loberto', 'Raimundo']
print("Enter a Name:")
name = input()
if name not in myPets:  # verifica se o nome esta contido na lista ou não atraves do boleano
    print("I dont know any " + name)
    while name not in myPets:
        print("Enter a Name:")
        name = input()
    if name in myPets:
        print(name + ' is my friend.')
else:
        print(name + ' is my friend.')
"""

#First Model that you can do when write a code this kind
cat = ['Fat', 'Black', 'Loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# Second option that you do is write this type of code more clean than the first
cat1 = ['Fat', 'Black', 'Loud']
size1, color1, disposition1 = cat1 # when you get this kind of code to do you need named all of part right
print('Size of cat is '+ size1)
print('Color of cat is '+ color1)




