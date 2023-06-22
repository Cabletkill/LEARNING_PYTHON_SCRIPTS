def eprimo(k):  #A função eprimo verifica se k e primo, caso seja ela returna True se nao False
    cont = 0
    for c in range(1, k + 1):
        if k % c == 0:
            cont += 1
    if cont <= 2:
        return True
    elif cont >= 3:
        return False

def maior_primo(k):  # recebe o numero primo verdadeiro e retorna, e enquanto for falso ele tira um e verifica novamente

    while eprimo(k) == False:
          #m = int(input('Digite o Valor de K:'))
          k -= 1
    print(k)
    ##return k


def entrada():  # entrada da variavel
    k = int(input('Digite o Valor de K:'))
    maior_primo(k)
entrada()