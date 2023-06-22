'''
1º Tuplas são imutaveis ou seja cada operação em uma tupla gera uma nova tupla
2º Listas são mutaveis podendo mudar costantemente
'''

meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
i=0
while i < len(meses):
        #print(meses[i])
        i = i + 1
        print(meses[i:])

print(meses.index('Março'))


