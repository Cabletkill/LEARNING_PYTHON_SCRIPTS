def main():
    x = int(input('Digite a Primeira Nota: '))
    y = int(input('Digite a Segunda Nota: '))
    enguanto(x,y)

def medias_notas(x, y):
    somanotas=(x+y)/2
    return somanotas

def enguanto(x,y):
    while x <= 0 or x > 10:
        print('Notas Invalidas')
        x = int(input('Digite a Primeira Nota: '))
    while y <= 0 or y > 10:
        print('Notas Invalidas')
        y = int(input('Digite a Segunda Nota: '))
    print('MEDIA = {:.2f}'.format(medias_notas(x, y)))

main()

