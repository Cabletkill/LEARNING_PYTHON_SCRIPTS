"""
#func com strings / métodos de strings
time = "    Ricardo de Souza Silva    "
print(time)

print(time.upper())#converte para letras maiusculas
print(time.lower())#converte para letras minusculas
print(time.capitalize())# transforma a primeira letra para maiuscula
print(time.strip())#remove os espacos em branco em excesso no começo ou no final da digitação

frases = "Ricardo gosta de comer banana e maça mais eu prefiro banana"

print(frases.count('banana'))#conta a quantidade letras ou palavras constão na frase ou na palavra
print(frases.count('a'))

print(frases.replace('banana', 'uva'))#efutua a troca da palavra ou letra
print(frases.center(70))#centraliza o texto conforme o solicitado
print(frases.find('g'))#procura a palavra ou txt
print(len(frases))#contador de str
print(frases[10:50])
"""
# conceitos para python
#def maiusculas(frase):
#def main():
 #    frase = ('PrOgRaMaMoS em python!')
  #   maiusculas(frase)


def maiusculas(frase):
    a = ""
    maiusculas02 = frase

    for i in range(len(frase)):
        if not frase[i] == maiusculas02.lower()[i]:
           a = a + frase[i]
    return a
 #   print(a)
#main()

