# função  principal
def main():
    '''
    Função principal, será a primeira a ser executado e
    será a responsável pela chamada de outras funções que
    por sua vez podem ou não chamar outras funçoes que
    por sua vez ...
    '''
    # corpo da função main
    x=int(input('Digite Numero='))
    função(x)

# Declaração das funções
def função(x):
    '''
    docstring da função f
    '''
    # corpo da função f
    soma=x**2
    return soma

def g():
    '''
    docstring da função g
    '''
    # corpo da função g
    print (main())

[...]

# início da execução do programa
main() # chamada da função main
print (função(x))