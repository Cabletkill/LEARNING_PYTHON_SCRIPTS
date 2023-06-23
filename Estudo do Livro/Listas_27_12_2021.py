spam = ['cat', 'bat', 'rat', 'elephant']
spam02 = ['cat', 'bat', 'rat', 'elephant','dog','rabit','elephant']
x=len(spam02)
for i in range(len(spam)):
    for j in range(0,x-1):
        if spam[i]==spam02[j]:
           del spam02[j]
           x = x - 1
print(spam)
print()
print(spam02)

