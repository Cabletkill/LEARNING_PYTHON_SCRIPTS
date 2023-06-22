import re

def main():
    assinatura = le_assinatura()
    lidos = le_textos()
    avalia_textos(lidos,assinatura)

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    return textos
def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)
def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()
def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas
def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    pass
def calcula_assinatura(texto):

    lista_de_palavras = separa_palavras(texto)
    tampalavras = 0
    contagem = 0
    for i in range(len(lista_de_palavras)):
        if conta[i] == ' ' or conta[i] == ',' or conta[i] == '.' or conta[i] == ';' or conta[i] == ':':
            contagem = contagem + 1
        else:
            tampalavras = tampalavras + 1
    tamanhomediodepalavra = tampalavras / len(ntpalavras.split())
    Type_Token= 0
    for i in range(len(lista_de_palavras.split())):
        for j in range(len(lista_de_palavras.split())):
            if conta[i] == conta02[j]:
                Type_Token = Type_Token + 1
                print(i, conta[i], j, conta02[j])
            else:
                Type_Token = Type_Token + 0

    assinatura = [tamanhomediodepalavra,Type_Token]
    return assinatura
    pass
def avalia_textos(textos, ass_cp):
    i = 1
    assinatura = calcula_assinatura(textos[i])
    similaridade = compara_assinatura(assinatura,ass_cp)
    menorgrau = similaridade
    infectado = i
    i = i + 1
    for i in range (0,len(textos)):
        assinatura = calcula_assinatura(textos[i])
        similaridade = compara_assinatura(assinatura, ass_cp)
        if similaridade < menorgrau:
            menorgrau = similaridade
            infectado = i
        i = i + 1
    print("O autor do texto %d está infectado com COH-PIAH" % (infectado))
    return infectado
    pass


main()

