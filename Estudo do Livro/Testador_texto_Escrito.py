supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
supplies2 = ['pens1', 'staplers', 'flame-throwers3', 'binders']

if len(supplies) == len(supplies2):
    for i in range(len(supplies)):
        if supplies[i] in supplies2:  # funcao in retira para fora da lista as palavras procuradas
            print(supplies[i])
