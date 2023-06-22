def fatorial(n):
    fatorial = 1

    while (n > 1):
        fatorial = fatorial * n
        n = n - 1
    return fatorial

def numero_binomial(n, k):
    fatorial()=int(input('digite'))
    return fatorial (n) / (fatorial (k) * fatorial (n-k) )

def test_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não Funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2 ")
    else:
        print("Não Funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0 ")
    else:
        print("Não Funciona para 0 ")
    if fatorial(5) == 120:
        print("Funciona para 5 ")
    else:
        print("Não Funciona para 5")
     
        
