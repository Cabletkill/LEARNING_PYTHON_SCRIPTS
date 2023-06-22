def primeiro():
    c = int(input('Digite o Conjunto: '))
    p = int(input('Digite o Grupo: '))

    fatorial = 1
    soma = 1
    while fatorial < c:
        fatorial = fatorial + 1
        soma = soma * fatorial
    print('Resultado conjunto:', soma)
    segundo(p)

def segundo(p):

    fatorial = 1
    soma1 = 1
    while fatorial < p:
        fatorial = fatorial + 1
        soma1 = soma1 * fatorial
    print('Resultado conjunto:', soma1)

primeiro()


