from random import randint

lista = ['Ricardo', 'Michele', 'Caue', 'Mario']
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
newlist = lista + spam

print(newlist)
listinha = ['cat', 'dog', 'bat']
x = 0
for line in newlist:
    if len(newlist) < 11:
        newlist.append(listinha[x])
        x += 1
print(newlist)
x = randint(1, 11)
y = len(newlist)

for line in newlist:
    if len(newlist) >= y:
        newlist.remove(newlist[x])
        y = len(newlist)
    else:
        continue
print(newlist)
